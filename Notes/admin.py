from django.contrib import admin
from .models import Tag,Note,DoList
# Register your models here.
admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(DoList)
