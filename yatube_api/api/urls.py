from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(
    r"posts/(?P<id>\d+)/comments",
    CommentViewSet,
    basename="Commentqrst",
)
router.register(r"groups", GroupViewSet)
router.register(r"follow", FollowViewSet, basename="Followqrst")

urlpatterns = [
    path("v1/", include(router.urls), name="api_urls"),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
