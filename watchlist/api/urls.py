from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist.api.views import movie_list, movie_details
from watchlist.api.views import (
    ReviewCreate,
    ReviewDetail,
    ReviewList,
    StreamPlatformAPIView,
    StreamPlatformDetailAPIView,
    WatchListAPIView,
    WathcListDetailAPIView,
    StreamPlatformViewSet,
)

# from watchlist.models import StreamPlatform

router = DefaultRouter()
router.register("stream", StreamPlatformViewSet, basename="streamplatform")

urlpatterns = [
    # path("list/", movie_list, name="movie-list"),
    # path("<int:pk>", movie_details, name="movie-details"),
    path("list/", WatchListAPIView.as_view(), name="movie-list"),
    path("<int:pk>", WathcListDetailAPIView.as_view(), name="movie-details"),
    # path("stream/", StreamPlatformAPIView.as_view(), name="stream"),
    # path(
    #     "stream/<int:pk>", StreamPlatformDetailAPIView.as_view(), name="stream-detail"
    # ),
    path("", include(router.urls)),
    path("stream/<int:pk>/review-create", ReviewCreate.as_view(), name="review-create"),
    path("stream/<int:pk>/review", ReviewList.as_view(), name="review-list"),
    path("stream/review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
]
