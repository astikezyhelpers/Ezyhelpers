from django.shortcuts import render, get_object_or_404
from .models import Blog, Services

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about-us.html')

def contact_us(request):
    return render(request, 'contact-us.html')

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