from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('services/', views.services, name='services'),
    path('service_details/<slug:slug>/', views.service_details, name='service_details'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<slug:slug>/', views.blog_details, name='blog_details'),
    
    # Thank You Page
    path('thank-you/', views.thank_you_view, name='thank_you'),

    # Main Service URLs - Each maps to the main_service_view with appropriate slug
    path('services/live-in-helpers/', views.main_service_view, {'slug': 'live-in-helpers'}, name='live_in_helpers'),
    path('services/full-time-helpers/', views.main_service_view, {'slug': 'full-time-helpers'}, name='full_time_helpers'),
    path('services/part-time-helpers/', views.main_service_view, {'slug': 'part-time-helpers'}, name='part_time_helpers'),
    path('services/on-demand-helpers/', views.main_service_view, {'slug': 'on-demand-helpers'}, name='on_demand_helpers'),
    path('services/nanny/', views.main_service_view, {'slug': 'nanny'}, name='nanny'),
    path('services/elderly-care/', views.main_service_view, {'slug': 'elderly-care'}, name='elderly_care'),
    path('services/cooks/', views.main_service_view, {'slug': 'cooks'}, name='cooks'),
    path('services/drivers/', views.main_service_view, {'slug': 'drivers'}, name='drivers'),
]