from rest_framework import serializers
from .models import Action, Notification, Author, AuthorBooks, Book, Genre, UserBooks, User, Role, Comment, Direction, \
    PublisherBooks
from drf_extra_fields.fields import Base64ImageField, Base64FileField



class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    image_path = Base64ImageField()
    class Meta:
        model = Author
        fields = '__all__'

class AuthorBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBooks
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    image_path = Base64ImageField()
    #pdf_path = Base64FileField()
    class Meta:
        model = Book
        fields = '__all__'

class BookLiteSerializer(serializers.ModelSerializer):
    image_path = Base64ImageField()
    class Meta:
        model = Book
        fields = ('name', 'description', 'year_of_creating', 'image_path', 'publisher', 'genre', 'is_deleted', 'delete_text', 'is_available')
class GenreSerializer(serializers.ModelSerializer):
    icon_path = Base64ImageField()
    class Meta:
        model = Genre
        fields = '__all__'



class UserBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBooks
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    avatar_path = Base64ImageField()
    class Meta:
        model = User
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'

class PublisherBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherBooks
        fields = '__all__'