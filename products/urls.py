from django.urls import path
from products.views import index, catalog, IndexListView


urlpatterns = [
    path("", IndexListView.as_view, name="index"),
    path("catalog/", catalog, name="catalog"),
]