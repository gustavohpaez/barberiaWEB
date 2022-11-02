from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='Tienda'),
    #path('widget/', views.widget, name='widget'),
    
]
