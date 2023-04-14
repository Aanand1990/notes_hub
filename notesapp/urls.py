from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:bookapp_id>', views.list_blog, name='list_blog'),
]
