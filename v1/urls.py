from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', auth),
    path('actions/', action_list_create),
    path('notifications/', notification_list_create),
    path('authors/', author_list_create),
    path('authorbooks/', authorbooks_list_create),
    path('books/', books_list_create),
    path('genres/', genres_list_create),
    path('userbooks/', userbooks_list_create),
    path('users/', users_list_create),
    path('actions/<int:pk>/', action_detail),
    path('notifications/<int:pk>/', notification_detail),
    path('authors/<int:pk>/', author_detail),
    path('authorbooks/<int:pk>/', authorbooks_detail),
    path('books/<int:pk>/', books_detail),
    path('genres/<int:pk>/', genres_detail),
    path('userbooks/<int:pk>/', userbooks_detail),
    path('books/get_by_user/<int:user>/', get_books_by_user),
    path('books/get_by_author/<int:author>/', get_books_by_author),
    path('books/get_by_genre/<int:genre>/', get_books_by_genre),
    path('users/get_by_role/<int:role>/', get_users_by_role_id),
    path('authors/get_by_book/<int:book_id>/', get_authors_by_book),
    path('users/<int:pk>/', users_detail),
    path('roles/', roles_list_create),
    path('roles/<int:pk>/', roles_detail),
    path('comments/', comments_list_create),
    path('comments/<int:pk>/', comments_detail),
    path('directions/', directions_list_create),
    path('directions/<int:pk>/', directions_detail),
    path('publisherbooks/', publisherbooks_list_create),
    path('publisherbooks/<int:pk>/', publisherbooks_detail),
]