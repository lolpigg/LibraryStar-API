from django.shortcuts import render
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from v1.models import *

from django.shortcuts import render

def main(request):
    return render(request, 'html/main.html')

class ActionCreateView(CreateView):
    model = Action
    template_name = 'html/create_form.html'
    form_class = ActionForm
    success_url = '../'


class ActionListView(ListView):
    model = Action
    template_name = 'html/list/action.html'  # Шаблон списка действий
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class ActionDetailView(DetailView):
    model = Action
    template_name = 'html/detail_form.html'  # Шаблон деталей действия
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class ActionUpdateView(UpdateView):
    model = Action
    form_class = ActionForm
    template_name = 'html/create_form.html'  # Шаблон обновления действия
    success_url = '../'

class ActionDeleteView(DeleteView):
    model = Action
    success_url = '../'
    template_name = 'html/delete_form.html'  # Шаблон подтверждения удаления действия

class NotificationCreateView(CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'html/create_form.html'
    success_url = '../'

class NotificationListView(ListView):
    model = Notification
    template_name = 'html/list/notification.html'  # Шаблон списка уведомлений
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'html/detail_form.html'  # Шаблон деталей уведомления
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = NotificationForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class NotificationUpdateView(UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'html/create_form.html'  # Шаблон обновления уведомления
    success_url = '../'

class NotificationDeleteView(DeleteView):
    model = Notification
    success_url = '../'
    template_name = 'html/delete_form.html'  # Шаблон подтверждения удаления уведомления

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'html/create_form.html'
    success_url = '../'

class AuthorListView(ListView):
    model = Author
    template_name = 'html/list/author.html'
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = AuthorForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'html/create_form.html'
    success_url = '../'

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '../'
    template_name = 'html/delete_form.html'


class AuthorBooksCreateView(CreateView):
    model = AuthorBooks
    form_class = AuthorBooksForm
    success_url = '../'
    template_name = 'html/create_form.html'

class AuthorBooksListView(ListView):
    model = AuthorBooks
    template_name = 'html/list/author_books.html'
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class AuthorBooksDetailView(DetailView):
    model = AuthorBooks
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class AuthorBooksUpdateView(UpdateView):
    model = AuthorBooks
    success_url = '../'
    form_class = AuthorBooksForm
    template_name = 'html/create_form.html'

class AuthorBooksDeleteView(DeleteView):
    model = AuthorBooks
    success_url = '../'
    template_name = 'html/delete_form.html'

class BookCreateView(CreateView):
    model = Book
    success_url = '../'
    form_class = BookForm
    template_name = 'html/create_form.html'

class BookListView(ListView):
    model = Book
    template_name = 'html/list/book.html'
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class BookUpdateView(UpdateView):
    model = Book
    success_url = '../'
    form_class = BookForm
    template_name = 'html/create_form.html'

class BookDeleteView(DeleteView):
    model = Book
    success_url = '../'
    template_name = 'html/delete_form.html'

class GenreCreateView(CreateView):
    model = Genre
    success_url = '../'
    form_class = GenreForm
    template_name = 'html/create_form.html'

class GenreListView(ListView):
    model = Genre
    template_name = 'html/list/genre.html'
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class GenreUpdateView(UpdateView):
    model = Genre
    success_url = '../'
    form_class = GenreForm
    template_name = 'html/create_form.html'

class GenreDeleteView(DeleteView):
    model = Genre
    success_url = '../'
    template_name = 'html/delete_form.html'

class UserBooksCreateView(CreateView):
    model = UserBooks
    form_class = UserBooksForm
    success_url = '../'
    template_name = 'html/create_form.html'

class UserBooksListView(ListView):
    model = UserBooks
    template_name = 'html/list/user_books.html'
    context_object_name = 'objects'
    success_url = '../'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class UserBooksDetailView(DetailView):
    model = UserBooks
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class UserBooksUpdateView(UpdateView):
    model = UserBooks
    form_class = UserBooksForm
    template_name = 'html/create_form.html'
    success_url = '../'

class UserBooksDeleteView(DeleteView):
    model = UserBooks
    success_url = '../'
    template_name = 'html/delete_form.html'

class PublisherBooksCreateView(CreateView):
    model = PublisherBooks
    form_class = PublisherBooksForm
    template_name = 'html/create_form.html'
    success_url = '../'

class PublisherBooksListView(ListView):
    model = PublisherBooks
    template_name = 'html/list/publisher_books.html'
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class PublisherBooksDetailView(DetailView):
    model = PublisherBooks
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    success_url = '../'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class PublisherBooksUpdateView(UpdateView):
    model = PublisherBooks
    form_class = PublisherBooksForm
    template_name = 'html/create_form.html'
    success_url = '../'

class PublisherBooksDeleteView(DeleteView):
    model = PublisherBooks
    success_url = '../'
    template_name = 'html/delete_form.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'html/create_form.html'
    success_url = '../'

class UserListView(ListView):
    model = User
    template_name = 'html/list/user.html'
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class UserDetailView(DetailView):
    model = User
    template_name = 'html/detail/users.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'html/create_form.html'
    success_url = '../'

class UserDeleteView(DeleteView):
    model = User
    success_url = '../'
    template_name = 'html/delete_form.html'

class RoleCreateView(CreateView):
    model = Role
    form_class = RoleForm
    success_url = '../'
    template_name = 'html/create_form.html'

class RoleListView(ListView):
    model = Role
    template_name = 'html/list/role.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context


class RoleDetailView(DetailView):
    model = Role
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class RoleUpdateView(UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'html/create_form.html'
    success_url = '../'

class RoleDeleteView(DeleteView):
    model = Role
    success_url = '../'
    template_name = 'html/delete_form.html'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = '../'
    template_name = 'html/create_form.html'

class CommentListView(ListView):
    model = Comment
    template_name = 'html/list/comment.html'
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = '../'
    template_name = 'html/create_form.html'


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = '../'
    template_name = 'html/delete_form.html'

class DirectionCreateView(CreateView):
    model = Direction
    form_class = DirectionForm
    success_url = '../'
    template_name = 'html/create_form.html'

class DirectionListView(ListView):
    model = Direction
    template_name = 'html/list/direction.html'
    context_object_name = 'objects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Создаем экземпляр формы
        russian_field_labels = [field.label for field in my_form]  # Получаем русскоязычные метки полей
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class DirectionDetailView(DetailView):
    model = Direction
    template_name = 'html/detail_form.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_form = ActionForm()  # Create an instance of the form
        russian_field_labels = [field.label for field in my_form]  # Get the Russian field labels
        context['form'] = my_form
        context['russian_field_labels'] = russian_field_labels
        return context

class DirectionUpdateView(UpdateView):
    model = Direction
    form_class = DirectionForm
    template_name = 'html/create_form.html'
    success_url = '../'

class DirectionDeleteView(DeleteView):
    model = Direction
    success_url = '../'
    template_name = 'html/delete_form.html'
