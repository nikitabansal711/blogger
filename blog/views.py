import datetime
import os
import uuid

import jwt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from dotenv import load_dotenv
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from werkzeug.security import generate_password_hash, check_password_hash

from blog.models import Post, User
from blog.serializers import PostSerializer, UserSerializer

load_dotenv()


class PostView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('comp')
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
            return Response({"success": "Blog '{}' created successfully".format(post_saved.title)})

    def put(self, request, pk):
        saved_post = get_object_or_404(Post, pk=pk)
        data = request.data.get('comp')
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
            return Response({"success": "Post '{}' updated successfully".format(post_saved.title)})

    def delete(self, request, pk):
        # Get object with this pk
        post = get_object_or_404(Post.objects.all(), pk=pk)
        Post.delete()
        return Response({"message": "Post with name `{}` has been deleted.".format(pk)}, post.title)


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})


class SignUp(APIView):
    def post(self, request):
        user = request.data.get("user")
        hashed_password = generate_password_hash(user["user_password"], method='sha256')
        user["user_password"] = hashed_password
        user["public_id "] = str(uuid.uuid4())
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({"success": "user '{}' created successfully".format(user_saved.user_name)})


class LoginView(APIView):
    def post(self, request):
        auth = request.data.get("auth")

        if not auth or not auth["username"] or not auth["password"]:
            return Response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

        user = User.objects.get(user_name=auth['username'])

        if not user:
            return Response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

        if check_password_hash(user.user_password, auth["password"]):
            token = jwt.encode(
                {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                os.getenv("SECRET_KEY"))

            return JsonResponse({'token': token.decode('UTF-8')})

        return Response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


def getByName(self, request):
    name = request.data.get('comp')
    post = Post.objects.filter(author=name)
    serializer = PostSerializer(post)
    return Response({"post": serializer.data})


def getByTitle(self, request):
    title = request.data.get('comp')
    post = Post.objects.filter(title=title)
    serializer = PostSerializer(post)
    return Response({"post": serializer.data})


@login_required
def home(request):
    return render(request, 'home.html')
