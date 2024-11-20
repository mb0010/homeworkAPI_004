from django.urls import path
from .views import*

urlpatterns = [
    # Author URLs
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),

    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    # Book URLs
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    # Borrow URLs
    path('borrows/', BorrowListCreateView.as_view(), name='borrow-list-create'),
    path('borrows/<int:pk>/', BorrowRetrieveUpdateDestroyView.as_view(), name='borrow-detail'),
]
