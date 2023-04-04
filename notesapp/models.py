from django.db import models


class BookApp(models.Model):
    book_cat_list = (('power_books','power_books'),
                     ('startup_books','startup_books'),
                     ('courses','courses'))
    book_name = models.CharField(max_length=200)
    book_category = models.CharField(max_length=200, choices= book_cat_list, default= 'power_books')

    def __str__(self):
        return self.book_name

class NotesApp(models.Model):
    notes_types_choices = (
        ("Notes", "Notes"),
        ("Excerpts", "Excerpts"),
        ("Insight", "Insight"),
    )
    notes_about = models.ForeignKey(BookApp, on_delete=models.CASCADE)
    notes_header = models.CharField(max_length=200)
    notes_type = models.CharField(max_length=200, choices= notes_types_choices, default= 'Notes')
    pub_date = models.DateTimeField(auto_now=True)
    notes_body = models.TextField(default=None)

    def __str__(self):
        return self.notes_header