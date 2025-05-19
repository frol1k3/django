from django.urls import path
from products.views import *


urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("catalog/", author_catalog, name="catalog"),
    path("catalog/", date_catalog, name="catalog"),
    path("all-authors/", api_get_all_authors, name="api_all_authors"),
    path("info/", info, name="info"),
    path("review/", review, name="review"),
    path("<int:pk>", book_card, name="book"),
    path("author/<int:pk>", author_card, name="author"),
]