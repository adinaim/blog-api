from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# from rest_framework.generics import (
#     ListAPIView, 
#     RetrieveAPIView, 
#     DestroyAPIView, 
#     UpdateAPIView, 
#     CreateAPIView
#     )

from .models import (
    Post, 
    Comment, 
    Tag
    )

from .serializers import (
    PostListSerailizer, 
    PostSerializer, 
    CommentSerializer
    )

from .permissions import IsOwner

    # один в один все
# class PostListView(ListAPIView):
#     # queryset = Post.objects.filter(status='open')
#     queryset = Post.objects.all()
#     serializer_class = PostListSerailizer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerailizer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return AllowAny
        elif self.action == 'create':
            return IsAuthenticated
        elif self.action in ['destroy', 'update', 'partial_update']:
            return IsOwner
        return super().get_permissions()
# комменты как подключаются

"""
actions

create() - POST
retrieve() - GET /post/1/
list() - GET /post/
destroy() - DELETE /post/1/
partial_update - PATCH /post/1
update() - PUT /post/1
"""
