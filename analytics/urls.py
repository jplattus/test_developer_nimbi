from django.urls import path

from analytics import views

urlpatterns = [
    path('create_navigation', views.create_navigation, name='create_navigation'),
    path('dashboard', views.dashboard, name='dashboard'),
]