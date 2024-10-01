from django.urls import path
from .views import  add_product, product_list, product_detail, delete_product
from .views import CreateProductView, ListProductsView, RetrieveProductView

urlpatterns = [
    path('api/products/create/', CreateProductView.as_view(), name='create_product'),  # Endpoint to create a product
    path('api/products/', ListProductsView.as_view(), name='list_products'),           # Endpoint to list all products
    path('api/products/<int:pk>/', RetrieveProductView.as_view(), name='retrieve_product'),  # Endpoint to retrieve a product by ID
    path('add/', add_product, name='add_product'),
    path('list/', product_list, name='product_list'),
    path('detail/<int:product_id>/', product_detail, name='product_detail'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
]

