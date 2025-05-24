from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Blog, Services, MainService, Lead
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Blog, Services, MainService, Lead
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

def home(request):
    success = False
    form_data_for_template = {}
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    if request.method == 'POST':
        # Grab values from POST
        service_needed = request.POST.get('service_needed')
        location = request.POST.get('location')
        phone = request.POST.get('contact_number')
        timing = request.POST.get('timing')

        # Prepare data for email, lead saving, and potential JSON response
        form_data = {
            'service_needed': service_needed,
            'location': location,
            'phone': phone,
            'timing': timing
        }
        form_data_for_template = form_data

        subject = 'New Helper Request from Home Page'
        message_body = f'''
        Service Needed: {service_needed}
        Location: {location}
        Contact Number: {phone}
        When Needed: {timing}
        '''
        try:
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, ['astik.ezyhelpers@gmail.com'])
            Lead.objects.create(
                phone=phone,
                service_needed=service_needed,
                location=location,
                timing=timing,
                source='Homepage'
            )
            success = True
            if is_ajax:
                return JsonResponse({'success': True, 'form_data': form_data})
        except Exception as e:
            print(f"Error processing homepage form: {e}")
            success = False
            if is_ajax:
                return JsonResponse({'success': False, 'error': 'An error occurred. Please try again.'}, status=500)
        
        # Non-AJAX fallback (might be removed if JS is required)
        # If JS is disabled, it will just re-render the page with success=True/False

    # Render for GET or non-AJAX POST 
    return render(request, 'home.html', {'success': success, 'form_data': form_data_for_template})

def about_us(request):
    return render(request, 'about-us.html')

def contact_us(request):
    success = False
    form_data_for_template = {}
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    if request.method == 'POST':
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        form_data = {
            'Name': full_name,
            'Email': email,
            'Phone': phone,
            'Message': message
        }
        form_data_for_template = form_data

        subject = 'Customer filled Contact Us Page Form'
        message_body = f'''
        Name: {full_name}
        Email: {email}
        Contact Number: {phone}
        Message: {message}
        '''
        try:
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, ['astik.ezyhelpers@gmail.com'])
            Lead.objects.create(
                name=full_name,
                email=email,
                phone=phone,
                message=message,
                source='Contact Us'
            )
            success = True
            if is_ajax:
                return JsonResponse({'success': True, 'form_data': form_data})
        except Exception as e:
            print(f"Error processing contact form: {e}")
            success = False
            if is_ajax:
                 return JsonResponse({'success': False, 'error': 'An error occurred. Please try again.'}, status=500)
        
        # Non-AJAX fallback

    return render(request, 'contact-us.html', {'success': success, 'form_data': form_data_for_template})

def services(request):
    services_list = Services.objects.all().order_by('-created_at')
    context = {'services': services_list}
    return render(request, 'services.html', context)

def service_details(request, slug):
    service = get_object_or_404(Services, slug=slug)
    context = {'service': service}
    return render(request, 'service_details.html', context)

def blogs(request):
    blog_posts = Blog.objects.all().order_by('-created_at')
    context = {'blogs': blog_posts}
    return render(request, 'blog.html', context)

def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {'blog': blog}
    return render(request, 'blog-details.html', context)

def main_service_view(request, slug):
    service = get_object_or_404(MainService, slug=slug)
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        form_data = {
            'Name': full_name,
            'Email': email,
            'Phone': phone,
            'Message': message
        }
        
        try:
            Lead.objects.create(
                name=full_name,
                email=email,
                phone=phone,
                message=message,
                source=f'Service Page: {service.name}'
            )

            subject = f'New Inquiry for {service.name}'
            email_message = f'''
            Service: {service.name}
            Name: {full_name}
            Email: {email}
            Contact Number: {phone}
            Message: {message}
            '''
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, ['astik.ezyhelpers@gmail.com'])
            
            if is_ajax:
                 # Add form_type to the data sent back for Thank You page generation
                response_data = form_data.copy()
                response_data['form_type'] = service.name
                return JsonResponse({'success': True, 'form_data': response_data})
            else:
                # Non-AJAX: Redirect to static thank you (won't have dynamic data)
                # Or redirect to the thank_you_view, passing data (less common for non-AJAX POST)
                return render(request, 'thankYou.html', { # Fallback render
                    'form_type': service.name,
                    'form_data': form_data 
                })
        
        except Exception as e:
            print(f"Error processing service page form for '{service.name}': {e}")
            if is_ajax:
                return JsonResponse({'success': False, 'error': 'An error occurred processing your request.'}, status=500)
            else:
                # Re-render form page on non-AJAX error
                 pass # Let it fall through to render below
    
    return render(request, 'services/main-service.html', {'service': service})

def main_service_view2(request, slug):
    service = get_object_or_404(MainService, slug=slug)
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        form_data = {
            'Name': full_name,
            'Email': email,
            'Phone': phone,
            'Message': message
        }
        
        try:
            Lead.objects.create(
                name=full_name,
                email=email,
                phone=phone,
                message=message,
                source=f'Service Page: {service.name}'
            )

            subject = f'New Inquiry for {service.name}'
            email_message = f'''
            Service: {service.name}
            Name: {full_name}
            Email: {email}
            Contact Number: {phone}
            Message: {message}
            '''
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, ['astik.ezyhelpers@gmail.com'])
            
            if is_ajax:
                 # Add form_type to the data sent back for Thank You page generation
                response_data = form_data.copy()
                response_data['form_type'] = service.name
                return JsonResponse({'success': True, 'form_data': response_data})
            else:
                # Non-AJAX: Redirect to static thank you (won't have dynamic data)
                # Or redirect to the thank_you_view, passing data (less common for non-AJAX POST)
                return render(request, 'thankYou.html', { # Fallback render
                    'form_type': service.name,
                    'form_data': form_data 
                })
        
        except Exception as e:
            print(f"Error processing service page form for '{service.name}': {e}")
            if is_ajax:
                return JsonResponse({'success': False, 'error': 'An error occurred processing your request.'}, status=500)
            else:
                # Re-render form page on non-AJAX error
                 pass # Let it fall through to render below
    
    return render(request, 'services/new-main-service.html', {'service': service})


def liveInHelpers(request):
    return main_service_view(request, 'live-in-helpers')

def fullTimeHelpers(request):
    return main_service_view(request, 'full-time-helpers')

def partTimeHelpers(request):
    return main_service_view(request, 'part-time-helpers')

def onDemandHelpers(request):
    return main_service_view(request, 'on-demand-helpers')

def nanny(request):
    return main_service_view(request, 'nanny')

def elderlyCare(request):
    return main_service_view(request, 'elderly-care')

def cooks(request):
    return main_service_view(request, 'cooks')

def drivers(request):
    return main_service_view(request, 'drivers')

def thank_you_view(request):
    form_items = []
    form_type = request.GET.get('form_type', 'Your Inquiry')
    for key, value in request.GET.items():
        if key != 'form_type' and value: # Exclude form_type and empty values
            form_items.append((key.replace("_"," "), value)) # Replace underscore and create tuple
    
    context = {
        'form_type': form_type,
        'form_items': form_items # Pass the list of tuples
    }
    return render(request, 'thankYou.html', context)

def submit_lead_form(request):
    if request.method == 'POST':
        service_id = request.POST.get('service')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service_date = request.POST.get('service_date')
        message = request.POST.get('message')
        
        try:
            service = MainService.objects.get(id=service_id)
            Lead.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=f"Service Date: {service_date}\n{message}",
                source=f'Service Page: {service.name}'
            )

            # Send email notification
            subject = f'New Service Booking Request - {service.name}'
            email_message = f'''
            Service: {service.name}
            Name: {name}
            Email: {email}
            Phone: {phone}
            Preferred Date: {service_date}
            Additional Requirements: {message}
            '''
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, ['astik.ezyhelpers@gmail.com'])
            
            # Handle AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you for your booking request. We will contact you shortly.'
                })
            
            # Redirect to thank you page with details
            from urllib.parse import urlencode
            base_url = reverse('thank_you')
            query_params = urlencode({
                'form_type': f'{service.name} Booking',
                'name': name,
                'email': email,
                'phone': phone,
                'service_date': service_date
            })
            redirect_url = f'{base_url}?{query_params}'
            return redirect(redirect_url)
            
        except Exception as e:
            print(f"Error processing lead form: {e}")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'error': 'An error occurred processing your request. Please try again.'
                }, status=500)
            
            # Re-render the form with error message
            messages.error(request, 'An error occurred processing your request. Please try again.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
    
    # If not POST, redirect back
    return redirect('/')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')