from django.db import models

class Action(models.Model):
    name = models.CharField(max_length=50)

class Notification(models.Model):
    description = models.CharField(max_length=1024)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    is_accepted = models.BooleanField()
    discard_text = models.CharField(max_length=1024)

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='img/authors/')
    year_of_birth = models.IntegerField()
    year_of_death = models.IntegerField(null=True)
    literary_direction = models.CharField(max_length=100)

class AuthorBooks(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Book(models.Model):
    name = models.CharField(max_length=255)
    number_of_pages = models.IntegerField()
    year_of_creating = models.IntegerField()
    image_path = models.ImageField(upload_to='img/books/')
    pdf_path = models.FileField(upload_to='pdf/')
    publisher = models.ForeignKey('User', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    is_deleted = models.BooleanField()
    delete_text = models.CharField(max_length=255, null=True)
    is_available = models.BooleanField()

class Genre(models.Model):
    name = models.CharField(max_length=50)
    icon_path = models.ImageField(upload_to='img/genres/')
    first_color = models.CharField(max_length=7)
    second_color = models.CharField(max_length=7)

class UserBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    registration_date = models.DateField()
    avatar_path = models.ImageField(null=True, upload_to='img/users/')
    last_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    last_book_page = models.IntegerField(null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    publisher_name = models.CharField(max_length=255, null=True)
    password_restore_date = models.DateField(null=True)

class Role(models.Model):
    name = models.CharField(max_length=50)
