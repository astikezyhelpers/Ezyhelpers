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
    
    # Legal Pages
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    
    # Form Submission URLs
    path('submit-lead-form/', views.submit_lead_form, name='submit_lead_form'),
    
    # Thank You Page
    path('thank-you/', views.thank_you_view, name='thank_you'),

    # New Service URLs using the new template
    path('services/new/live-in-helpers/', views.main_service_view2, {'slug': 'live-in-helpers'}, name='new_live_in_helpers'),
    path('services/new/full-time-helpers/', views.main_service_view2, {'slug': 'full-time-helpers'}, name='new_full_time_helpers'),
    path('services/new/part-time-helpers/', views.main_service_view2, {'slug': 'part-time-helpers'}, name='new_part_time_helpers'),
    path('services/new/on-demand-helpers/', views.main_service_view2, {'slug': 'on-demand-helpers'}, name='new_on_demand_helpers'),
    path('services/new/nanny/', views.main_service_view2, {'slug': 'nanny'}, name='new_nanny'),
    path('services/new/elderly-care/', views.main_service_view2, {'slug': 'elderly-care'}, name='new_elderly_care'),
    path('services/new/cooks/', views.main_service_view2, {'slug': 'cooks'}, name='new_cooks'),
    path('services/new/drivers/', views.main_service_view2, {'slug': 'drivers'}, name='new_drivers'),
    path('services/new/full-time-maid-service/', views.main_service_view2, {'slug': 'full-time-maid-service'}, name='new_full_time_maid_service'),

    # Original Service URLs (keeping these for now until the new template is approved)
    path('services/live-in-helpers/', views.main_service_view, {'slug': 'live-in-helpers'}, name='live_in_helpers'),
    path('services/full-time-helpers/', views.main_service_view, {'slug': 'full-time-helpers'}, name='full_time_helpers'),
    path('services/part-time-helpers/', views.main_service_view, {'slug': 'part-time-helpers'}, name='part_time_helpers'),
    path('services/on-demand-helpers/', views.main_service_view, {'slug': 'on-demand-helpers'}, name='on_demand_helpers'),
    path('services/nanny/', views.main_service_view, {'slug': 'nanny'}, name='nanny'),
    path('services/elderly-care/', views.main_service_view, {'slug': 'elderly-care'}, name='elderly_care'),
    path('services/cooks/', views.main_service_view, {'slug': 'cooks'}, name='cooks'),
    path('services/drivers/', views.main_service_view, {'slug': 'drivers'}, name='drivers'),
]