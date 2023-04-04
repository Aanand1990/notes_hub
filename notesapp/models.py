from django.db import models


class BookApp(models.Model):
    book_cat_list = ['power_books', 'startup_books', 'courses']
    book_name = models.CharField(max_length=200)
    book_category = models.CharField(max_length=200, choices=book_cat_list, default=1)


class NotesApp(models.Model):
    notes_about = models.ForeignKey(BookApp)
    notes_header = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    notes_body = models.TextField(default=None)
