from rest_framework import serializers

from blog.models import User, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'updated_on', 'content', 'created_on')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_mobile', 'user_email', 'user_address','user_password','profile_photo','public_id')
