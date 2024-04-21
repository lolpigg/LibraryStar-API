from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'actions', ActionViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'author-books', AuthorBooksViewSet)
router.register(r'books', BookViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'user-books', UserBooksViewSet)
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/auth/<str:login>/<str:password>/', auth),
]