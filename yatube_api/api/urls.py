from django.urls import include, path
from rest_framework import routers

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register(r"posts", PostViewSet, basename="posts")
v1_router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet,
                   basename="comments"
                   )
v1_router.register(r"groups", GroupViewSet, basename="groups")
v1_router.register(r"follow", FollowViewSet, basename='followers')

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path('v1/auth/', include('djoser.urls.jwt')),
]
