from django.db import models
# from ckeditor.fields import RichTextField # Remove old
from django.contrib.auth.models import User
from django.utils.text import slugify
# from ckeditor_uploader.fields import RichTextUploadingField # Remove old
from django_ckeditor_5.fields import CKEditor5Field
import math
import re

# Custom CKEditor configurations (These are for CKEditor 4 and no longer used)
# CKEDITOR_BASIC_CONFIG = { ... }
# CKEDITOR_FULL_CONFIG = { ... }

class Services(models.Model):
    name = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    meta_description = models.TextField()
    content = CKEditor5Field(config_name='default')
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
    content = CKEditor5Field(config_name='default')
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
        # Simplified reading time calculation - consider a library for HTML stripping if needed
        word_count = len(re.sub('<[^<]+?>', ' ', self.content if self.content else '').split())
        return max(1, math.ceil(word_count / 200))

# New Models for Service Features
class ServiceFeature(models.Model):
    service = models.ForeignKey('MainService', related_name='custom_features', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fas fa-check')")
    description = CKEditor5Field(config_name='default')
    
    def __str__(self):
        return self.title

class ServiceStat(models.Model):
    service = models.ForeignKey('MainService', related_name='custom_stats', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fas fa-star')")
    description = CKEditor5Field(config_name='default')
    
    def __str__(self):
        return self.title

class FAQ(models.Model):
    service = models.ForeignKey('MainService', related_name='custom_faqs', on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=200)
    answer = CKEditor5Field(config_name='default')
    
    def __str__(self):
        return self.question

# New Model for How It Works Steps
class HowItWorksStep(models.Model):
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = CKEditor5Field(config_name='default')
    icon = models.CharField(max_length=50, blank=True, help_text="Optional: FontAwesome class (e.g., 'fas fa-check')")
    service = models.ForeignKey('MainService', related_name='how_it_works_steps', on_delete=models.CASCADE)

    class Meta:
        ordering = ['step_number'] # Order steps naturally

    def __str__(self):
        return f"{self.step_number}. {self.title}"

# New Model for Benefits
class Benefit(models.Model):
    title = models.CharField(max_length=150)
    description = CKEditor5Field(config_name='default')
    icon = models.CharField(max_length=50, blank=True, help_text="Optional: FontAwesome class (e.g., 'fas fa-check-circle')")
    service = models.ForeignKey('MainService', related_name='benefits', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# New Model for Specialized Service Details
class SpecializedServiceDetail(models.Model):
    title = models.CharField(max_length=150)
    description = CKEditor5Field(config_name='default')
    icon = models.CharField(max_length=50, blank=True, help_text="Optional: FontAwesome class")
    service = models.ForeignKey('MainService', related_name='specialized_details', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# New Model for Consideration Points
class ConsiderationPoint(models.Model):
    point_text = CKEditor5Field(config_name='default')
    icon = models.CharField(max_length=50, blank=True, default='fas fa-info-circle', help_text="Optional: FontAwesome class (defaults to info icon)")
    service = models.ForeignKey('MainService', related_name='consideration_points', on_delete=models.CASCADE)

    def __str__(self):
        # Basic string representation, might need refinement if point_text is long HTML
        return self.point_text[:50] + '...' if self.point_text and len(self.point_text) > 50 else (self.point_text or '')

class MainService(models.Model):
    # Basic Info
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    
    # Hero Section
    hero_title = CKEditor5Field(config_name='default')
    hero_subtitle = CKEditor5Field(config_name='default')
    hero_image = models.ImageField(upload_to='static/service_images/')
    hero_rating = models.DecimalField(max_digits=3, decimal_places=2, default=4.98)
    
    # Features Section
    features_title = models.CharField(max_length=200)
    
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