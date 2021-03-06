from django.db.models import Count, Avg
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from reviews.models import Review
from reviews.serializers import ReviewSerializer, ShopListReviewSerializer, ShopListRatingSerializer


class CreateReviewAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UpdateDeleteReviewAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ListShopAPIView(ListAPIView):
    serializer_class = ShopListReviewSerializer

    def get_queryset(self):
        method = self.request.GET
        if method.get('review_count', None):
            queryset = Review.objects.values('domain_name').annotate(review_count=Count('id')).order_by('-review_count')
        elif method.get('rating_count', None):
            self.serializer_class = ShopListRatingSerializer
            queryset = Review.objects.values('domain_name').annotate(avg_star_count=Avg('star_count')).order_by('-avg_star_count')
        elif method.get('author_email', None):
            self.serializer_class = ReviewSerializer
            queryset = Review.objects.filter(author_email=method.get('author_email')).order_by('created_at')
        elif method.get('name', None):
            self.serializer_class = ReviewSerializer
            queryset = Review.objects.filter(domain_name=method.get('name'))
        else:
            self.serializer_class = ReviewSerializer
            queryset = Review.objects.all()
        return queryset



