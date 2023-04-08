from django.shortcuts import render, get_object_or_404
from .models import BookApp, NotesApp


def home(request):
    books = list(BookApp.objects.all())
    return render(request, 'home.html', {'books': books})


def list_blog(request, bookapp_id):
    book_notes = list(NotesApp.objects.filter(notes_about=bookapp_id))
    return render(request, 'book_notes.html', {'book_notes': book_notes})
