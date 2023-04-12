from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse_lazy


class CategoryModel(models.Model):
    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    img = models.ImageField(
        upload_to='category/img',
        default='category/img/logo.png'
    )

    description = models.TextField()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse_lazy('catalog:category_list_url')


class ProductModel(models.Model):
    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    available = models.BooleanField(
        default=True
    )

    description = models.TextField()

    price = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=0,
                message='Ціна не може бути негативною!')
        ]
    )

    amount = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(
                limit_value=0,
                message='Кількість може бути негативним значенням!')
        ]
    )

    img = models.ImageField(
        upload_to='catalog/img',
        default='category/img/logo.png'
    )

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse_lazy('catalog:product_detail_url', kwargs={'product_slug': self.slug})
