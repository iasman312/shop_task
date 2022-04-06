from django.urls import path

from reviews.views import (
    CreateReviewAPIView,
    UpdateDeleteReviewAPIView, ListShopAPIView,
)

urlpatterns = [
    path('', CreateReviewAPIView.as_view(), name='review-create'),
    path('<int:pk>/', UpdateDeleteReviewAPIView.as_view(), name='review-update_delete'),
    path('shops/search/', ListShopAPIView.as_view(), name='shop-list')
]