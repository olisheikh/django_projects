from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.home_view, name="home_view"),
    # path('products/<int:id>/', views.product_details, name="product_details"),
    path('products/add_product', views.add_product, name="add_product"),
    path('products/cls/', views.ProductListView.as_view(), name="product_list"),
    path('products/<int:pk>/', views.ProductDetails.as_view(), name="product_view_cls"),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name="product_edit"),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name="product_delete"),
    path('products/api', views.product_api, name='product_api'),
]