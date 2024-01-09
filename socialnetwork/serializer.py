# serializers.py
from rest_framework import serializers

from users.serializer import UserResponseSerializer
from .models import Blogs, Like


class LikeSerializerResponse(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class BlogsSerializerResponse(serializers.ModelSerializer):
    author = UserResponseSerializer()
    liked_blog = LikeSerializerResponse(many=True)

    class Meta:
        model = Blogs
        fields = "__all__"


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ['title', 'content']

    def create(self, validated_data):
        user_id = self.context.get('user', None)
        blog = Blogs.objects.create(title=validated_data.get('title', None),
                                    content=validated_data.get('content', None), author_id=user_id)
        return blog


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
