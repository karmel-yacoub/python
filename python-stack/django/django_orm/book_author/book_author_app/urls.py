from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

                    
urlpatterns =[
    path('',views.books), 
    path('add_book',views.add_books),
    path('books/<int:b_id>',views.view_book),
    path('add_auth_to_book/<int:b_id>',views.add_auth_to_book),
    path('authors',views.authors),
    path('add_author',views.add_author),
    path('authors/<int:a_id>',views.view_author),
    path('add_book_to_auth/<int:a_id>',views.add_book_to_auth)

]