from django.shortcuts import render
from products.models import *
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse
from django.urls import reverse

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
    date = req.GET.get("date")
    books = Book.objects.all() 
    if (author):
        books = books.filter(authors=author)
    if (date):
        books = Book.objects.filter(date_public__year__gt=int(date))       
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

def book_card(request: HttpRequest, pk: int):
    if (pk):
        book = Book.objects.get(id=pk)
        author = Author.objects.filter(books=book)[0]
        return render(request, "book_card.html", {"book":book, "author":author})
    return reverse("catalog")

def author_card(request: HttpRequest, pk: int):
    if (pk):
        author = Author.objects.get(id=pk)
        return render(request, "author_card.html", {"author":author})
    return reverse("book_card.html")


