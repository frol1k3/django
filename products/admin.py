from django.contrib import admin
from products.models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)
admin.site.register(User)