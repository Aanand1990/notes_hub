# Generated by Django 4.2 on 2023-04-04 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('book_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NotesApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_header', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('notes_body', models.TextField(default=None)),
                ('notes_about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notesapp.bookapp')),
            ],
        ),
    ]
