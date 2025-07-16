from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    register,
    admin_view,
    librarian_view,
    member_view,
    list_books,  # Explicitly imported
    add_book,
    edit_book,
    delete_book,
    LibraryDetailView,
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    path('list_books/', list_books, name='list_books'),  # Directly using the imported function
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),

    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
