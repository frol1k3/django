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

def author_catalog(req: HttpRequest):
    #Достаю параметр маршрута
    author = req.GET.get("author")
    if (author):
        books = Book.objects.filter(authors=author)
    else:
        books = Book.objects.all()    
    return render(req, "catalog.html", {"books": books})

def date_catalog(req: HttpRequest):
    date = req.GET.get("date")
    if (date):
        for book in books:
            if book.date_publick.year >= date:
                books = Book.objects.filter(books=book)    
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


