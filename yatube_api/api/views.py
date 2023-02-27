from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Follow
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAuthenticated

from .pagination import PostsPagination
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, GroupSerializer, \
    CommentSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostsPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly)
    pagination_class = PostsPagination


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return post.comments


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated)
