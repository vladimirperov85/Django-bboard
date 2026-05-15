# Django/Django-bboard/shop/urls.py

from django.urls import path
from . import views  # Импортируем views из текущей папки

# Имя приложения — пригодится позже, когда будем делать ссылки
app_name = "shop"

urlpatterns = [
    # path('') — пустой путь = главная страница
    # views.product_list — какая view обрабатывает
    # name='product_list' — имя маршрута (для создания ссылок в шаблонах)
    path("", views.product_list, name="product_list"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path('category/<slug:category_slug>/', views.products_by_category, name='products_by_category')
    
]
