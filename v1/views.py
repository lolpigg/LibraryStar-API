from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import io
import base64

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'

@api_view(['GET'])
def get_users_by_role_id(request, role):
    try:
        users = User.objects.filter(role=role)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_books_by_user(request, user):
    try:
        user_books = UserBooks.objects.filter(user=user, is_active=True)
        books = [user_book.book for user_book in user_books]
        book_data = []
        for book in books:
            book_info = {
                'id': book.id,
                'name': book.name,
                'description': book.description,
                'year_of_creating': book.year_of_creating,
                'image_path': request.build_absolute_uri(book.image_path.url) if book.image_path else None,
                'pdf_path': "",
                'publisher': book.publisher.id,
                'genre': book.genre.id,
                'is_deleted': book.is_deleted,
                'delete_text': book.delete_text,
                'is_available': book.is_available
            }
            book_data.append(book_info)
        return Response(book_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_books_by_author(request, author):
    try:
        user_books = AuthorBooks.objects.filter(author=author)
        books = [user_book.book for user_book in user_books]
        book_data = []
        for book in books:
            book_info = {
                'id': book.id,
                'name': book.name,
                'description': book.description,
                'year_of_creating': book.year_of_creating,
                'image_path': request.build_absolute_uri(book.image_path.url) if book.image_path else None,
                'pdf_path': "",
                'publisher': book.publisher.id,
                'genre': book.genre.id,
                'is_deleted': book.is_deleted,
                'delete_text': book.delete_text,
                'is_available': book.is_available
            }
            book_data.append(book_info)
        return Response(book_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_books_by_genre(request, genre):
    try:
        books = Book.objects.filter(genre=genre)
        book_data = []
        for book in books:
            book_info = {
                'id': book.id,
                'name': book.name,
                'description': book.description,
                'year_of_creating': book.year_of_creating,
                'image_path': request.build_absolute_uri(book.image_path.url) if book.image_path else None,
                'pdf_path': "",
                'publisher': book.publisher.id,
                'genre': book.genre.id,
                'is_deleted': book.is_deleted,
                'delete_text': book.delete_text,
                'is_available': book.is_available
            }
            book_data.append(book_info)
        return Response(book_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_authors_by_book(request, book_id):
    try:
        # Получаем книгу по переданному ID
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    # Получаем все записи AuthorBooks, связанные с этой книгой
    author_books = AuthorBooks.objects.filter(book=book)

    # Формируем список авторов
    authors = [
        {
            'id': author_book.author.id,
            'full_name': author_book.author.full_name,
            'image_path': request.build_absolute_uri(author_book.author.image_path.url) if author_book.author.image_path else None,
            'year_of_birth': author_book.author.year_of_birth,
            'year_of_death': author_book.author.year_of_death,
        }
        for author_book in author_books
    ]

    # Возвращаем список авторов в формате JSON
    return Response(authors, status=status.HTTP_200_OK)


@api_view(['POST'])
def auth(request):
    if request.method == 'POST':
        login = request.data.get('login')
        password = request.data.get('password')
        if login is None or password is None:
            return Response({'error': 'Please provide both login and password'}, status=400)
        try:
            user = get_object_or_404(User, login=login, password=password)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=400)
    else:
        return Response({'error': 'Only POST method is allowed'}, status=405)


@api_view(['GET', 'POST'])
def action_list_create(request):
    if request.method == 'GET':
        paginator = CustomPagination()
        actions = Action.objects.all()
        result_page = paginator.paginate_queryset(actions, request)
        serializer = ActionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def action_detail(request, pk):
    try:
        action = Action.objects.get(pk=pk)
    except Action.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActionSerializer(action)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ActionSerializer(action, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        action.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def notification_list_create(request):
    if request.method == 'GET':
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def notification_detail(request, pk):
    try:
        notification = Notification.objects.get(pk=pk)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NotificationSerializer(notification, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def author_list_create(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(author, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def authorbooks_list_create(request):
    if request.method == 'GET':
        author_books = AuthorBooks.objects.all()
        serializer = AuthorBooksSerializer(author_books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorBooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def authorbooks_detail(request, pk):
    try:
        author_book = AuthorBooks.objects.get(pk=pk)
    except AuthorBooks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorBooksSerializer(author_book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AuthorBooksSerializer(author_book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        author_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def books_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        book_data = []
        for book in books:
            book_info = {
                'id': book.id,
                'name': book.name,
                'description': book.description,
                'year_of_creating': book.year_of_creating,
                'image_path': request.build_absolute_uri(book.image_path.url) if book.image_path else None,
                'pdf_path': "",
                'publisher': book.publisher.id,
                'genre': book.genre.id,
                'is_deleted': book.is_deleted,
                'delete_text': book.delete_text,
                'is_available': book.is_available
            }
            book_data.append(book_info)
        return Response(book_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def books_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def genres_list_create(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        image_data = data.get('icon_path')

        # Декодируем изображение из base64
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))

        # Сохраняем изображение в формате PNG
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')

        # Получаем байтовое представление изображения
        image_png = buffer.getvalue()

        # Модифицируем данные, чтобы сохранить байтовое представление изображения
        data['icon_path'] = base64.b64encode(image_png).decode('utf-8')
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def genres_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        image_data = data.get('icon_path')

        # Декодируем изображение из base64
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))

        # Сохраняем изображение в формате PNG
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')

        # Получаем байтовое представление изображения
        image_png = buffer.getvalue()

        # Модифицируем данные, чтобы сохранить байтовое представление изображения
        data['icon_path'] = base64.b64encode(image_png).decode('utf-8')
        serializer = GenreSerializer(genre, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def userbooks_list_create(request):
    if request.method == 'GET':
        user_books = UserBooks.objects.all()
        serializer = UserBooksSerializer(user_books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        book_id = data.get('book')
        user_id = data.get('user')

        try:
            user_book = UserBooks.objects.get(book_id=book_id, user_id=user_id)
            if not user_book.is_active:
                user_book.is_active = True
                user_book.save()
                serializer = UserBooksSerializer(user_book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User book already exists and is active'}, status=status.HTTP_400_BAD_REQUEST)
        except UserBooks.DoesNotExist:
            serializer = UserBooksSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def userbooks_detail(request, pk):
    try:
        user_book = UserBooks.objects.get(pk=pk)
    except UserBooks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserBooksSerializer(user_book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserBooksSerializer(user_book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def users_list_create(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def roles_list_create(request):
    if request.method == 'GET':
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def roles_detail(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(role, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def comments_list_create(request):
    if request.method == 'GET':
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def comments_detail(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def directions_list_create(request):
    if request.method == 'GET':
        direction = Direction.objects.all()
        serializer = DirectionSerializer(direction, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DirectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def directions_detail(request, pk):
    try:
        direction = Direction.objects.get(pk=pk)
    except Direction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DirectionSerializer(direction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DirectionSerializer(direction, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        direction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def publisherbooks_list_create(request):
    if request.method == 'GET':
        publisher_books = PublisherBooks.objects.all()
        serializer = PublisherBooksSerializer(publisher_books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublisherBooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def publisherbooks_detail(request, pk):
    try:
        publisher_books = PublisherBooks.objects.get(pk=pk)
    except PublisherBooks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PublisherBooksSerializer(publisher_books)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublisherBooksSerializer(publisher_books, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        publisher_books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
