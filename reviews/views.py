from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class CreateReviewAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UpdateDeleteReviewAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

