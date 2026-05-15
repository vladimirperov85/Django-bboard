# Django/Django-bboard/shop/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Category


def product_list(request):
    """
    View для отображения списка всех товаров.
    request — это объект запроса от браузера (всё, что прислал пользователь).
    """
    # Достаём из БД все товары, которые есть в наличии (available=True)
    # order_by('name') — сортируем по имени
    products = Product.objects.filter(available=True).order_by("name")

    # render — функция, которая "склеивает" шаблон с данными
    # 'shop/product/list.html' — путь к шаблону
    # {'products': products} — словарь данных, который попадёт в шаблон
    return render(request, "shop/product/list.html", {"products": products})


def product_detail(request, slug):
    """
    View для отображения одного товара.
    slug приходит из URL (например: /product/gamer-pro-rtx-4060/).
    """
    # get_object_or_404 ищет товар по slug. Если не находит — показывает страницу 404
    product = get_object_or_404(Product, slug=slug, available=True)

    return render(request, "shop/product/detail.html", {"product": product})


def products_by_category(request, category_slug):
    """
    View для отображения товаров одной категории.
    category_slug приходит из URL (например: /category/igrovye-sborki/).
    """
    # Находим категорию по slug (или 404, если нет)
    category = get_object_or_404(Category, slug=category_slug)

    # Фильтруем товары: только этой категории + доступные
    products = Product.objects.filter(category=category, available=True)

    return render(
        request, "shop/category.html", {"category": category, "products": products}
    )
