from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории товаров: Игровые, Офисные и т.д."""

    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, verbose_name="URL-идентификатор"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """Товары (сборки ПК)"""

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, db_index=True, verbose_name="URL-идентификатор"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="В наличии")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")

    class Meta:
        ordering = ["name"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        indexes = [
            models.Index(fields=["id", "slug"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
