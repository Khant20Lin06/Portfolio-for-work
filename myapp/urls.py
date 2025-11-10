from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomePage, name="homePage"),
    path('message/', views.message, name='messagePage'),
]