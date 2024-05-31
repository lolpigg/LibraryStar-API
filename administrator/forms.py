from django.forms import forms

from django import forms
from v1.models import (Action, Notification, Author, AuthorBooks, Book, Genre, UserBooks, PublisherBooks, User, Role, Comment, Direction)

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['name']
        labels = {'name': 'Название'}

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['description', 'action', 'book', 'is_accepted', 'discard_text']
        labels = {
            'description': 'Описание',
            'action': 'Действие',
            'book': 'Книга',
            'is_accepted': 'Принято',
            'discard_text': 'Текст отмены'
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'image_path', 'year_of_birth', 'year_of_death', ]
        labels = {
            'full_name': 'ФИО',
            'image_path': 'Фотография',
            'year_of_birth': 'Год рождения',
            'year_of_death': 'Год смерти',
        }

class AuthorBooksForm(forms.ModelForm):
    class Meta:
        model = AuthorBooks
        fields = ['author', 'book']
        labels = {'author': 'Автор', 'book': 'Книга'}

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'year_of_creating', 'image_path', 'pdf_path', 'publisher', 'genre', 'is_deleted', 'delete_text', 'is_available']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'year_of_creating': 'Год создания',
            'image_path': 'Изображение',
            'pdf_path': 'PDF файл',
            'publisher': 'Издатель',
            'genre': 'Жанр',
            'is_deleted': 'Удалено',
            'delete_text': 'Текст удаления',
            'is_available': 'Доступно'
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'icon_path', 'first_color', 'second_color']
        labels = {
            'name': 'Название',
            'icon_path': 'Иконка',
            'first_color': 'Первый цвет',
            'second_color': 'Второй цвет'
        }
    def __init__(self, *args, **kwargs):
        super(GenreForm, self).__init__(*args, **kwargs)
        self.fields['icon_path'].required = False

class UserBooksForm(forms.ModelForm):
    class Meta:
        model = UserBooks
        fields = ['book', 'user', 'is_active']
        labels = {'book': 'Книга', 'user': 'Пользователь', 'is_active': 'Активно'}

class PublisherBooksForm(forms.ModelForm):
    class Meta:
        model = PublisherBooks
        fields = ['book', 'publisher', 'is_active']
        labels = {'book': 'Книга', 'publisher': 'Издатель', 'is_active': 'Активно'}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'avatar_path', 'role', 'publisher_name']
        labels = {
            'login': 'Логин',
            'avatar_path': 'Аватар',
            'role': 'Роль',
            'publisher_name': 'Название издателя'
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']
        labels = {'name': 'Название'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['book', 'user', 'mark', 'text']
        labels = {'book': 'Книга', 'user': 'Пользователь', 'mark': 'Оценка', 'text': 'Текст'}

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['name', 'description', 'year_of_found']
        labels = {'name': 'Название', 'description': 'Описание', 'year_of_found': 'Год основания'}
