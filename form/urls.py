from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('success/', views.registration_success, name='registration_success'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
