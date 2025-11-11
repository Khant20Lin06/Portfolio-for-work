from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomePage, name="homePage"),
    path('projectSingle/<uuid:pk>/', views.ProjectSinglePage, name="projectSinglePage"),
    path('message/', views.message, name='messagePage'),
]