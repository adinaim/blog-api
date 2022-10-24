from rest_framework import serializers

from .models import(
    Post,
    Tag,
    Comment
)

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title', 'image']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = '__all__'

    # def validate(self, attrs):
        # request = self.context.get('request')
        # user = request.user
        # attrs['user'] = user
        # return attrs


class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()

    class Meta:
        model = Post
        exclude = ['user']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['id']