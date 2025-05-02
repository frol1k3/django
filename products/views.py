from django.shortcuts import render
from products.models import *
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse


class IndexListView (ListView):
    model = Book 
    template_name = "index.html"
    context_object_name = "books"

#def index(req):
#   books = Book.objects.all()
#   return render(req, "index.html", {"books" : books})

def catalog(req: HttpRequest):
    #Достаю параметр маршрута
    author = req.GET.get("author")
    if (author):
        books = Book.objects.filter(authors=author)
    else:
        books = Book.objects.all()    
    return render(req, "catalog.html", {"books": books})

def api_get_all_authors(req):
    authors = Author.objects.all()
    dataList = [author.parse_object() for author in authors]
    # list - чтобы преобразовать объект класса QuerySet в массив
    return JsonResponse(dataList, safe=False)

def info(req):
    return render(req, "info.html")

def review(req):
    user = req.GET.get("user")
    if (user):
        reviews = Review.objects.filter(reviews=review)
    else:
        reviews = Review.objects.all()    
    return render(req, "review.html", {"reviews": reviews})