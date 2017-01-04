from django.contrib import admin
from .models import Note,ListDo,ListContent
# Register your models here.
admin.site.register(Note)
#admin.site.register(Tag)
admin.site.register(ListDo)
admin.site.register(ListContent)
#admin.site.register(ListDoTag)
# admin.site.register(NoteTag)
#admin.site.register(UserTag)

