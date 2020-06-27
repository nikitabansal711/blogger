from rest_framework import serializers

from .models import Page, Stat


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('topic', 'content', 'blog', 'updated_on', 'created_on', 'status')


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ('pageViews', 'page')
