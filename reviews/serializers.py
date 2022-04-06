import re
from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'ecommerce_link',
            'title',
            'text',
            'star_count',
            'author_email',
        )
        model = Review

    def create(self, validated_data):
        ecommerce_link = validated_data.get('ecommerce_link')
        m = re.search('https?://([A-Za-z_0-9.-]+).*', ecommerce_link)
        if m:
            domain_name = m.group(1).split('.')[0]
            validated_data['domain_name'] = domain_name
        return super().create(validated_data)


