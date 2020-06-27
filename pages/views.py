from django.conf import settings
from django.core.mail import send_mail
from django.forms.models import model_to_dict
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from twilio.rest import Client

from blog.models import Post, Followers
from .models import Page, Stat
from .serializer import PageSerializer, StatSerializer


class PageView(APIView):
    def get(self, request):
        title = request.data.get("comp")
        blog = Post.objects.get(title=title)
        pages = Page.objects.filter(blog=blog)
        for page in pages:

            stat = Stat.objects.filter(page=page)
            if len(stat) != 0:
                stat = Stat.objects.get(page=page)
                stat.pageViews = stat.pageViews + 1
                temp = {
                    # "page": stat.page.page_id,
                    "pageViews": stat.pageViews
                }
                serializer = StatSerializer(instance=stat, data=temp, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
            else:
                temp = {
                    "page": page.pk,
                    "pageViews": 1
                }
                serializer = StatSerializer(data=temp)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

        # paginator = Paginator(pages, 10)
        serializer = PageSerializer(pages, many=True)
        return Response({"pages": serializer.data})

    def post(self, request):
        page = request.data.get('comp')
        serializer = PageSerializer(data=page)
        if serializer.is_valid(raise_exception=True):
            page_saved = serializer.save()
            followers = Followers.objects.filter(blog_followed=page_saved.blog)
            recipient_list = []
            for temp in followers:
                recipient_list.append(temp.follower.user_email)
                to = '+91' + temp.follower.user_mobile
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                response = client.messages.create(
                    body='dear follower, your favourite post got a new page',
                    to=to, from_=settings.TWILIO_PHONE_NUMBER)
            subject = 'post updated'
            message = 'dear follower, your favourite post has got a new page'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, recipient_list)

            return Response({"success": "page '{}' created successfully".format(page_saved.blog.title)})

    def put(self, request, pk):
        saved_page = get_object_or_404(Page, pk=pk)
        data = request.data.get('comp')
        serializer = PageSerializer(instance=saved_page, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            page_saved = serializer.save()
            return Response({"success": "Post '{}' updated successfully".format(page_saved.topic)})


class AllPages(APIView):
    def get(self, request, pk):
        page = get_object_or_404(Page.objects.all(), pk=pk)
        temp = model_to_dict(page)
        serializer = PageSerializer(data=temp)
        if serializer.is_valid(raise_exception=True):
            return Response({"page": serializer.data})


class StatView(APIView):
    def get(self, request):
        id = request.data.get('id')
        page = Page.objects.get(pk=id)
        stat = Stat.objects.get(page=page)
        temp = model_to_dict(stat)
        serializer = StatSerializer(data=temp)
        if serializer.is_valid(raise_exception=True):
            return Response({"stat": serializer.data})
