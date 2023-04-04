from django.contrib import admin

from .models import BookApp, NotesApp

admin.site.register(BookApp)
admin.site.register(NotesApp)
