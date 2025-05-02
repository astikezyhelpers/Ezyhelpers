from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
import math
import re

# Custom CKEditor configurations
CKEDITOR_BASIC_CONFIG = {
    'toolbar': 'Basic',
    'height': 200,
    'width': '100%',
    'toolbar_Basic': [
        ['Bold', 'Italic', 'Underline', 'Strike', 'TextColor', 'BGColor'],
        ['Link', 'Unlink'],
        ['NumberedList', 'BulletedList'],
        ['Undo', 'Redo'],
    ],
}

CKEDITOR_FULL_CONFIG = {
    'toolbar': 'Full',
    'height': 300,
    'width': '100%',
    'toolbar_Full': [
        ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'TextColor', 'BGColor'],
        ['Link', 'Unlink'],
        ['Image', 'Table', 'HorizontalRule'],
        ['NumberedList', 'BulletedList'],
        ['Indent', 'Outdent'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['Source'],
        ['Undo', 'Redo'],
    ],
    'extraPlugins': 'justify,textcolor,colorbutton,font',
}

class Services(models.Model):
    name = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    meta_description = models.TextField()
    content = RichTextField()
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    image = models.ImageField(upload_to='static/blog_images/', default='static/images/ezyhelpers.png')
    content = RichTextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    reading_time = models.PositiveIntegerField(editable=False, default=5)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.reading_time = self.calculate_reading_time()
        super().save(*args, **kwargs)

    def calculate_reading_time(self):
        word_count = len(re.sub('<[^<]+?>', ' ', self.content).split())
        return max(1, math.ceil(word_count / 200))

# New Models for Service Features
class ServiceFeature(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)  # FontAwesome class
    description = RichTextField(config_name='basic')
    
    def __str__(self):
        return self.title

class ServiceStat(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)  # FontAwesome class
    description = RichTextField(config_name='basic')
    
    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = RichTextField(config_name='basic')
    
    def __str__(self):
        return self.question

# New Model for How It Works Steps
class HowItWorksStep(models.Model):
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='basic')
    icon = models.CharField(max_length=50, blank=True, help_text="Optional: FontAwesome class (e.g., 'fas fa-check')")
    service = models.ForeignKey('MainService', related_name='how_it_works_steps', on_delete=models.CASCADE)

    class Meta:
        ordering = ['step_number'] # Order steps naturally

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"

# New Model for Benefits
class Benefit(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='basic')
    icon = models.CharField(max_length=50, blank=True, help_text="Optional: FontAwesome class (e.g., 'fas fa-check-circle')")
    service = models.ForeignKey('MainService', related_name='benefits', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# New Model for Specialized Service Details
class SpecializedServiceDetail(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='basic')
    icon = models.CharField(max_length=50, blank=True, help_text="Optional: FontAwesome class")
    service = models.ForeignKey('MainService', related_name='specialized_details', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# New Model for Consideration Points
class ConsiderationPoint(models.Model):
    point_text = RichTextField(config_name='basic', help_text="The text for the consideration point.")
    icon = models.CharField(max_length=50, blank=True, default='fas fa-info-circle', help_text="Optional: FontAwesome class (defaults to info icon)")
    service = models.ForeignKey('MainService', related_name='consideration_points', on_delete=models.CASCADE)

    def __str__(self):
        # Basic string representation, might need refinement if point_text is long HTML
        return self.point_text[:50] + '...' if len(self.point_text) > 50 else self.point_text

class MainService(models.Model):
    # Basic Info
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    
    # Hero Section
    hero_title = RichTextField(config_name='basic')
    hero_subtitle = RichTextField(config_name='basic')
    hero_image = models.ImageField(upload_to='static/service_images/')
    hero_rating = models.DecimalField(max_digits=3, decimal_places=2, default=4.98)
    
    # Stats Section
    stats = models.ManyToManyField(ServiceStat)
    
    # Features Section
    features_title = models.CharField(max_length=200)
    features = models.ManyToManyField(ServiceFeature)
    
    # How It Works
    how_it_works_title = models.CharField(max_length=200)
    
    # Benefits
    benefits_title = models.CharField(max_length=200)
    benefits_link_text = models.CharField(max_length=100, blank=True)
    benefits_link_url = models.CharField(max_length=200, blank=True)
    
    # Specialized Services
    specialized_services_title = models.CharField(max_length=200)
    
    # Considerations
    considerations_title = models.CharField(max_length=200)
    
    # FAQs
    faqs = models.ManyToManyField(FAQ)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# Universal Lead Model for All Forms
class Lead(models.Model):
    SOURCE_CHOICES = [
        ('Homepage', 'Homepage Quick Quote'),
        ('Contact Us', 'Contact Us Page'),
        ('Service Page', 'Service Page Quote'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255, help_text="Full name of the lead")
    email = models.EmailField(max_length=255, help_text="Email address")
    phone = models.CharField(max_length=20, help_text="Contact phone number")
    message = models.TextField(blank=True, help_text="Message or inquiry details")
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, help_text="Where the lead originated from")
    
    # Optional fields primarily from homepage form
    service_needed = models.CharField(max_length=255, null=True, blank=True, help_text="Service requested (Homepage)")
    location = models.CharField(max_length=255, null=True, blank=True, help_text="Location provided (Homepage)")
    timing = models.CharField(max_length=100, null=True, blank=True, help_text="When service is needed (Homepage)")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead from {self.get_source_display()} - {self.name} ({self.email}) - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-created_at']