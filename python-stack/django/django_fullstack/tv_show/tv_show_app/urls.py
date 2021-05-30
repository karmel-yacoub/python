from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('new',views.form),
    path('create',views.create),
    path('<int:the_id>',views.information),
    path('<int:c_id>/edit',views.edit),
    path('<int:e_id>/update',views.update),
    path('<int:d_id>/destroy',views.destroy),
    
]
