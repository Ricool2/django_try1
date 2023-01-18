#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_main, name = 'books_main'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>', views.BooksDetail.as_view(), name = 'booksdetail'),
    path('<int:pk>/update', views.BooksUpdate.as_view(), name = 'booksupdate')

]