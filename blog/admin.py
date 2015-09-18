from django.contrib import admin
from blog.models import Author,Artical,Tag,Classification
# Register your models here.
admin.site.register(Author)
admin.site.register(Artical)
admin.site.register(Tag)
admin.site.register(Classification)