from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    ecommerce_link = models.URLField(
        _('Ecommerce link'),
        max_length=500,
    )
    title = models.CharField(
        _('Review title'),
        max_length=300,
    )
    text = models.TextField(
        _('Review text'),
        max_length=3000,
    )
    star_count = models.PositiveSmallIntegerField(
        _('Stars count'),
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
    )
    author_email = models.EmailField(
        _('Reviews author email'),
    )
    domain_name = models.CharField(
        _('Domain name'),
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = _('reviews')
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')


