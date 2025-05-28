from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import RegexValidator
import math
import re

# Add slug validator
slug_validator = RegexValidator(
    regex=r'^[a-z0-9-]+$',
    message="Slug can only contain lowercase letters, numbers, and hyphens"
)

class Services(models.Model):
    name = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    meta_description = models.TextField()
    content = CKEditor5Field(config_name='default')
    slug = models.SlugField(max_length=100, unique=True, validators=[slug_validator], editable=True)
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
    slug = models.SlugField(max_length=200, unique=True, validators=[slug_validator], editable=True)
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
    slug = models.SlugField(max_length=100, unique=True, validators=[slug_validator], editable=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    
    # 1. Hero Section (Required)
    hero_title = CKEditor5Field(config_name='default')
    hero_subtitle = CKEditor5Field(config_name='default')
    hero_image = models.ImageField(upload_to='static/service_images/')
    hero_image_alt_text = models.CharField(max_length=200, blank=True, null=True)
    hero_rating = models.DecimalField(max_digits=3, decimal_places=2, default=4.98)
    
    # 2. Service Stats Section (Required)
    stats_title = models.CharField(max_length=200)
    stats_subtitle = models.TextField()
    stats_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the stats section")
    
    # 3. Features Section (Required)
    features_title = models.CharField(max_length=200)
    features_subtitle = models.TextField()
    features_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the features section")
    
    # 4. Specialized Services Section (Optional)
    specialized_services_title = models.CharField(max_length=200, blank=True, null=True)
    specialized_services_subtitle = models.TextField(blank=True, null=True)
    specialized_services_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the specialized services section")
    
    # 5. Types of Services Section (Optional)
    service_types_title = models.CharField(max_length=200, blank=True, null=True)
    service_types_subtitle = models.TextField(blank=True, null=True)
    service_types_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the service types section")
    
    # 6. Benefits Section (Optional)
    benefits_title = models.CharField(max_length=200, blank=True, null=True)
    benefits_subtitle = models.TextField(blank=True, null=True)
    benefits_link_text = models.CharField(max_length=100, blank=True)
    benefits_link_url = models.CharField(max_length=200, blank=True)
    benefits_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the benefits section")
    
    # 7. Choose Right Service Section (Optional)
    choose_service_title = models.CharField(max_length=200, blank=True, null=True)
    choose_service_subtitle = models.TextField(blank=True, null=True)
    choose_service_image = models.ImageField(upload_to='static/service_images/', null=True, blank=True)
    choose_service_image_alt_text = models.CharField(max_length=200, blank=True, null=True)
    choose_service_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the choose service section")
    
    # 8. Why Hire Us Section (Optional)
    why_hire_title = models.CharField(max_length=200, blank=True, null=True)
    why_hire_subtitle = models.TextField(blank=True, null=True)
    why_hire_image = models.ImageField(upload_to='static/service_images/', null=True, blank=True)
    why_hire_image_alt_text = models.CharField(max_length=200, blank=True, null=True)
    why_hire_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the why hire us section")
    
    # 9. Ideal For Section (Optional)
    ideal_for_title = models.CharField(max_length=200, blank=True, null=True)
    ideal_for_subtitle = models.TextField(blank=True, null=True)
    ideal_for_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the ideal for section")
    
    # 10. How to Book Section (Required)
    how_to_book_title = models.CharField(max_length=200)
    how_to_book_subtitle = models.TextField()
    how_to_book_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the how to book section")
    
    # 11. Key Considerations Section (Required)
    considerations_title = models.CharField(max_length=200)
    considerations_subtitle = models.TextField()
    considerations_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the considerations section")
    
    # 12. Hyperlinks Section (Required)
    hyperlinks_title = models.CharField(max_length=200)
    hyperlinks_subtitle = models.TextField()
    
    # 13. CTA Section (Required)
    cta_title = models.CharField(max_length=200)
    cta_subtitle = models.TextField()
    cta_bottom_paragraph = CKEditor5Field(config_name='default', blank=True, help_text="Additional text to appear below the CTA section")
    
    # 14. Lead Form Section (Required)
    lead_form_title = models.CharField(max_length=200)
    lead_form_subtitle = models.TextField()
    lead_form_image = models.ImageField(upload_to='static/service_images/', null=True, blank=True)
    lead_form_image_alt_text = models.CharField(max_length=200, blank=True, null=True)
    
    # 15. FAQs Section (Required)
    faqs_title = models.CharField(max_length=200)
    faqs_subtitle = models.TextField()
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def check_required_sections(self):
        """Check if all required sections are complete"""
        required_sections = {
            'Hero Section': all([self.hero_title, self.hero_subtitle, self.hero_image]),
            'Service Stats Section': all([self.stats_title, self.stats_subtitle]),
            'Features Section': all([self.features_title, self.features_subtitle]),
            'How to Book Section': all([self.how_to_book_title, self.how_to_book_subtitle]),
            'Key Considerations Section': all([self.considerations_title, self.considerations_subtitle]),
            'Hyperlinks Section': all([self.hyperlinks_title, self.hyperlinks_subtitle]),
            'CTA Section': all([self.cta_title, self.cta_subtitle, self.cta_button_text, self.cta_secondary_button_text]),
            'Lead Form Section': all([self.lead_form_title, self.lead_form_subtitle]),
            'FAQs Section': all([self.faqs_title, self.faqs_subtitle])
        }
        return required_sections

    class Meta:
        verbose_name = "Main Service"
        verbose_name_plural = "Main Services"
        ordering = ['-created_at']

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

# New Model for Service Types Cards
class ServiceTypeCard(models.Model):
    service = models.ForeignKey('MainService', related_name='service_type_cards', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = CKEditor5Field(config_name='default')
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fas fa-home')")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

# New Model for Ideal For Cards
class IdealForCard(models.Model):
    service = models.ForeignKey('MainService', related_name='ideal_for_cards', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = CKEditor5Field(config_name='default')
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fas fa-home')")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

# New Model for How to Book Steps
class BookingStep(models.Model):
    service = models.ForeignKey('MainService', related_name='booking_steps', on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = CKEditor5Field(config_name='default')
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fas fa-calendar')")
    
    class Meta:
        ordering = ['step_number']
    
    def __str__(self):
        return f"{self.step_number}. {self.title}"

# New Model for Hyperlinks Cards
class HyperlinkCard(models.Model):
    service = models.ForeignKey('MainService', related_name='hyperlink_cards', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = CKEditor5Field(config_name='default')
    link_text = models.CharField(max_length=100)
    link_url = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fas fa-link')")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

# New Model for Why Choose Us Points
class WhyChooseUsPoint(models.Model):
    service = models.ForeignKey('MainService', related_name='why_choose_us_points', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fas fa-check-circle')")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

# New Model for Choosing Right Points
class ChoosingRightPoint(models.Model):
    service = models.ForeignKey('MainService', related_name='choosing_right_points', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fas fa-check-circle')")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title