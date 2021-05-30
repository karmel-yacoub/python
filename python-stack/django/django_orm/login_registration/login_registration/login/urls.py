from django.urls.resolvers import URLPattern
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('registration',views.registration),
    path('sucsess',views.sucsess),
    path ('logout',views.logout),
    path('login',views.login)
    
]