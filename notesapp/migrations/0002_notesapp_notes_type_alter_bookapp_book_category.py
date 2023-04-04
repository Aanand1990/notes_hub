# Generated by Django 4.2 on 2023-04-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesapp',
            name='notes_type',
            field=models.CharField(choices=[('Notes', 'Notes'), ('Excerpts', 'Excerpts'), ('Insight', 'Insight')], default='Notes', max_length=200),
        ),
        migrations.AlterField(
            model_name='bookapp',
            name='book_category',
            field=models.CharField(choices=[('power_books', 'power_books'), ('startup_books', 'startup_books'), ('courses', 'courses')], default='power_books', max_length=200),
        ),
    ]
