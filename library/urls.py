from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path("books/", views.BookListView.as_view(), name="books_list"),
    path("books/new", views.BookCreateView.as_view(), name="book_create"),
    path("books/detail/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/update/<int:pk>/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/delete/<int:pk>/", views.BookDeleteView.as_view(), name="book_delete"),
    path("author/new/", views.AuthorCreateView.as_view(), name="author_create"),
    path(
        "authors/update/<int:pk>/",
        views.AuthorUpdateView.as_view(),
        name="author_update",
    ),
    path("authors/", views.AuthorListView.as_view(), name="authors_list"),
    path(
        "books/recommend/<int:pk>/",
        views.RecommendBookView.as_view(),
        name="book_recommend",
    ),
    path("books/review/<int:pk>/", views.ReviewBookView.as_view(), name="book_review"),
]
