from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Action, Notification, Author, AuthorBooks, Book, Genre, UserBooks, User, Role
from .serializers import ActionSerializer, NotificationSerializer, AuthorSerializer, AuthorBooksSerializer, BookSerializer, GenreSerializer, UserBooksSerializer, UserSerializer, RoleSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorBooksViewSet(viewsets.ModelViewSet):
    queryset = AuthorBooks.objects.all()
    serializer_class = AuthorBooksSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class UserBooksViewSet(viewsets.ModelViewSet):
    queryset = UserBooks.objects.all()
    serializer_class = UserBooksSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# def auth(request, login, password):
#     users = User.objects.all()
#     for user in users:
#         if user.login == login and user.password == password:
#             return user.id
#     return -1

@api_view(['GET'])
def auth(request, login, password):
    try:
        user = User.objects.get(login=login, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=400)