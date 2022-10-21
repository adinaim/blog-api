from rest_framework import serializers

from .models import(
    Post,
    Tag,
    Comment
)

class PostListSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title', 'image']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['id']