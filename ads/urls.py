from django.urls import path

from ads.apps import AdsConfig
from ads.views import (
    AdsCreateAPIView,
    AdsDestroyAPIView,
    AdsListAPIView,
    AdsRetrieveAPIView,
    AdsUpdateAPIView,
    FeedbackCreateAPIView,
    FeedbackDestroyAPIView,
    FeedbackListAPIView,
    FeedbackRetrieveAPIView,
    FeedbackUpdateAPIView
)

app_name = AdsConfig.name

urlpatterns = [
    path("ads/create/", AdsCreateAPIView.as_view(), name="ads_create"),
    path("ads/", AdsListAPIView.as_view(), name="ads_list"),
    path("ads/retrieve/<int:pk>/", AdsRetrieveAPIView.as_view(), name="ads_retrieve"),
    path("ads/update/<int:pk>/", AdsUpdateAPIView.as_view(), name="ads_update"),
    path("ads/destroy/<int:pk>/", AdsDestroyAPIView.as_view(), name="ads_destroy"),
    path("feedback/create/", FeedbackCreateAPIView.as_view(), name="feedback_create"),
    path("feedback/", FeedbackListAPIView.as_view(), name="feedback_list"),
    path("feedback/retrieve/<int:pk>/", FeedbackRetrieveAPIView.as_view(), name="feedback_retrieve"),
    path("feedback/update/<int:pk>/", FeedbackUpdateAPIView.as_view(), name="feedback_update"),
    path("feedback/destroy/<int:pk>/", FeedbackDestroyAPIView.as_view(), name="feedback_destroy"),
]
