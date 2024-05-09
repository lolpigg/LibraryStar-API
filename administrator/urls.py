from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    # URLs for Action model
    path('action/create/', views.ActionCreateView.as_view(), name='action_create'),
    path('action/<int:pk>/', views.ActionDetailView.as_view(), name='action_detail'),
    path('action/<int:pk>/update/', views.ActionUpdateView.as_view(), name='action_update'),
    path('action/<int:pk>/delete/', views.ActionDeleteView.as_view(), name='action_delete'),
    path('action/', views.ActionListView.as_view(), name='action_list'),

    # URLs for Notification model
    path('notification/create/', views.NotificationCreateView.as_view(), name='notification_create'),
    path('notification/<int:pk>/', views.NotificationDetailView.as_view(), name='notification_detail'),
    path('notification/<int:pk>/update/', views.NotificationUpdateView.as_view(), name='notification_update'),
    path('notification/<int:pk>/delete/', views.NotificationDeleteView.as_view(), name='notification_delete'),
    path('notification/', views.NotificationListView.as_view(), name='notification_list'),

    # URLs for Author model
    path('author/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    path('author/', views.AuthorListView.as_view(), name='author_list'),

    # URLs for AuthorBooks model
    path('authorbooks/create/', views.AuthorBooksCreateView.as_view(), name='authorbooks_create'),
    path('authorbooks/<int:pk>/', views.AuthorBooksDetailView.as_view(), name='authorbooks_detail'),
    path('authorbooks/<int:pk>/update/', views.AuthorBooksUpdateView.as_view(), name='authorbooks_update'),
    path('authorbooks/<int:pk>/delete/', views.AuthorBooksDeleteView.as_view(), name='authorbooks_delete'),
    path('authorbooks/', views.AuthorBooksListView.as_view(), name='authorbooks_list'),

    # URLs for Book model
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('book/', views.BookListView.as_view(), name='book_list'),

    # URLs for Genre model
    path('genre/create/', views.GenreCreateView.as_view(), name='genre_create'),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('genre/<int:pk>/update/', views.GenreUpdateView.as_view(), name='genre_update'),
    path('genre/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre_delete'),
    path('genre/', views.GenreListView.as_view(), name='genre_list'),

    # URLs for UserBooks model
    path('userbooks/create/', views.UserBooksCreateView.as_view(), name='userbooks_create'),
    path('userbooks/<int:pk>/', views.UserBooksDetailView.as_view(), name='userbooks_detail'),
    path('userbooks/<int:pk>/update/', views.UserBooksUpdateView.as_view(), name='userbooks_update'),
    path('userbooks/<int:pk>/delete/', views.UserBooksDeleteView.as_view(), name='userbooks_delete'),
    path('userbooks/', views.UserBooksListView.as_view(), name='userbooks_list'),

    # URLs for PublisherBooks model
    path('publisherbooks/create/', views.PublisherBooksCreateView.as_view(), name='publisherbooks_create'),
    path('publisherbooks/<int:pk>/', views.PublisherBooksDetailView.as_view(), name='publisherbooks_detail'),
    path('publisherbooks/<int:pk>/update/', views.PublisherBooksUpdateView.as_view(), name='publisherbooks_update'),
    path('publisherbooks/<int:pk>/delete/', views.PublisherBooksDeleteView.as_view(), name='publisherbooks_delete'),
    path('publisherbooks/', views.PublisherBooksListView.as_view(), name='publisherbooks_list'),

    # URLs for User model
    path('user/create/', views.UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('user/', views.UserListView.as_view(), name='user_list'),

    # URLs for Role model
    path('role/create/', views.RoleCreateView.as_view(), name='role_create'),
    path('role/<int:pk>/', views.RoleDetailView.as_view(), name='role_detail'),
    path('role/<int:pk>/update/', views.RoleUpdateView.as_view(), name='role_update'),
    path('role/<int:pk>/delete/', views.RoleDeleteView.as_view(), name='role_delete'),
    path('role/', views.RoleListView.as_view(), name='role_list'),

    # URLs for Comment model
    path('comment/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/', views.CommentListView.as_view(), name='comment_list'),

    # URLs for Direction model
    path('direction/create/', views.DirectionCreateView.as_view(), name='direction_create'),
    path('direction/<int:pk>/', views.DirectionDetailView.as_view(), name='direction_detail'),
    path('direction/<int:pk>/update/', views.DirectionUpdateView.as_view(), name='direction_update'),
    path('direction/<int:pk>/delete/', views.DirectionDeleteView.as_view(), name='direction_delete'),
    path('direction/', views.DirectionListView.as_view(), name='direction_list'),
]
