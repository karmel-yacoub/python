from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('dojos',views.creat),
    path('ninjas',views.add),
    # path('',views.show)
]