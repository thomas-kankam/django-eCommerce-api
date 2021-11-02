from django.urls import path
from .views import ListCategory, DetialedCategory, ListBook, DetialedBook, ListProduct, DetialedProduct
urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetialedCategory.as_view(), name='singleCategory'),
    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>/', DetialedBook.as_view(), name='singleBook'),
    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetialedProduct.as_view(), name='singleProduct')
]
