from django.urls import path

from reviews.views import (
    CreateReviewAPIView,
    UpdateDeleteReviewAPIView,
)

urlpatterns = [
    path('', CreateReviewAPIView.as_view(), name='review-create'),
    path('<int:pk>/', UpdateDeleteReviewAPIView.as_view(), name='review-update_delete')
]