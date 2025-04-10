from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('services', views.services, name='services'),
    path('service_details/<slug:slug>/', views.service_details, name='service_details'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/<slug:slug>/', views.blog_details, name='blog_details'),
]