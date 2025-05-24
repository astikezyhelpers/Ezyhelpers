from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import slugify
from .models import (
    Blog, Services, MainService, ServiceFeature, ServiceStat, FAQ, HowItWorksStep,
    Benefit, SpecializedServiceDetail, ConsiderationPoint, Lead,
    ServiceTypeCard, IdealForCard, BookingStep, HyperlinkCard, SpecializedServiceCard
)

class CustomInlineMixin:
    """Mixin to add common functionality to all inline admin classes"""
    extra = 0  # Don't show extra empty forms by default
    classes = ('collapse',)  # Make sections collapsible
    show_change_link = True  # Allow direct editing of inline items

class CustomServiceStatInline(CustomInlineMixin, admin.StackedInline):
    model = ServiceStat
    fields = (
        ('title', 'icon'),
        'description'
    )
    verbose_name = "Service Statistic"
    verbose_name_plural = "1. Service Statistics"
    help_text = "Add statistics that highlight key aspects of your service"

class CustomServiceFeatureInline(CustomInlineMixin, admin.StackedInline):
    model = ServiceFeature
    fields = (
        ('title', 'icon'),
        'description'
    )
    verbose_name = "Service Feature"
    verbose_name_plural = "2. Service Features"
    help_text = "Add features that describe what your service offers"

class HowItWorksStepInline(CustomInlineMixin, admin.StackedInline):
    model = HowItWorksStep
    fields = (
        ('step_number', 'title'),
        'icon',
        'description'
    )
    verbose_name = "How It Works Step"
    verbose_name_plural = "3. How It Works Steps"
    ordering = ['step_number']
    help_text = "Add steps to explain your service process"

class BenefitInline(CustomInlineMixin, admin.StackedInline):
    model = Benefit
    fields = (
        ('title', 'icon'),
        'description'
    )
    verbose_name = "Benefit"
    verbose_name_plural = "4. Benefits"
    help_text = "Add benefits that customers get from your service"

class SpecializedServiceDetailInline(CustomInlineMixin, admin.StackedInline):
    model = SpecializedServiceDetail
    fields = (
        ('title', 'icon'),
        'description'
    )
    verbose_name = "Specialized Service Detail"
    verbose_name_plural = "5. Specialized Service Details"
    help_text = "Add specialized aspects of your service"

class ConsiderationPointInline(CustomInlineMixin, admin.StackedInline):
    model = ConsiderationPoint
    fields = (
        'icon',
        'point_text'
    )
    verbose_name = "Consideration Point"
    verbose_name_plural = "6. Consideration Points"
    help_text = "Add important points to consider about your service"

class CustomFAQInline(CustomInlineMixin, admin.StackedInline):
    model = FAQ
    fields = (
        'question',
        'answer'
    )
    verbose_name = "FAQ"
    verbose_name_plural = "7. FAQs"
    help_text = "Add frequently asked questions and their answers"

class ServiceTypeCardInline(CustomInlineMixin, admin.StackedInline):
    model = ServiceTypeCard
    fields = (
        ('title', 'icon'),
        'description',
        ('image', 'order')
    )
    verbose_name = "Service Type"
    verbose_name_plural = "8. Service Types"
    help_text = "Add different types of services you offer"
    ordering = ['order']

class IdealForCardInline(CustomInlineMixin, admin.StackedInline):
    model = IdealForCard
    fields = (
        ('title', 'icon'),
        'description',
        'order'
    )
    verbose_name = "Ideal For Card"
    verbose_name_plural = "9. Ideal For Cards"
    help_text = "Add cards describing who your service is ideal for"
    ordering = ['order']

class BookingStepInline(CustomInlineMixin, admin.StackedInline):
    model = BookingStep
    fields = (
        ('step_number', 'title'),
        'icon',
        'description'
    )
    verbose_name = "Booking Step"
    verbose_name_plural = "10. Booking Steps"
    help_text = "Add steps explaining how to book your service"
    ordering = ['step_number']

class HyperlinkCardInline(CustomInlineMixin, admin.StackedInline):
    model = HyperlinkCard
    fields = (
        ('title', 'icon'),
        'description',
        ('link_text', 'link_url'),
        'order'
    )
    verbose_name = "Hyperlink Card"
    verbose_name_plural = "11. Hyperlink Cards"
    help_text = "Add cards with links to related services and resources"
    ordering = ['order']

class SpecializedServiceCardInline(CustomInlineMixin, admin.StackedInline):
    model = SpecializedServiceCard
    fields = (
        ('title', 'icon'),
        'description',
        ('image', 'order')
    )
    verbose_name = "Specialized Service"
    verbose_name_plural = "12. Specialized Services"
    help_text = "Add cards for specialized services you offer"
    ordering = ['order']

@admin.register(MainService)
class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_hero_image', 'created_at', 'updated_at', 'display_stats_count', 'display_features_count')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'meta_title', 'meta_description', 'hero_title', 'hero_subtitle')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'preview_hero_image', 'preview_choose_service_image', 
                      'preview_why_hire_image', 'preview_lead_form_image')
    save_on_top = True
    
    def preview_hero_image(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 200px;" />', obj.hero_image.url)
        return "No image"
    preview_hero_image.short_description = "Hero Image Preview"

    def preview_choose_service_image(self, obj):
        if obj.choose_service_image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 200px;" />', obj.choose_service_image.url)
        return "No image"
    preview_choose_service_image.short_description = "Choose Service Image Preview"

    def preview_why_hire_image(self, obj):
        if obj.why_hire_image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 200px;" />', obj.why_hire_image.url)
        return "No image"
    preview_why_hire_image.short_description = "Why Hire Us Image Preview"

    def preview_lead_form_image(self, obj):
        if obj.lead_form_image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 200px;" />', obj.lead_form_image.url)
        return "No image"
    preview_lead_form_image.short_description = "Lead Form Image Preview"

    def display_hero_image(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="max-width: 50px; max-height: 50px;" />', obj.hero_image.url)
        return "No image"
    display_hero_image.short_description = "Hero"

    def display_stats_count(self, obj):
        return obj.custom_stats.count()
    display_stats_count.short_description = "Stats"

    def display_features_count(self, obj):
        return obj.custom_features.count()
    display_features_count.short_description = "Features"
    
    fieldsets = (
        ('1. Basic Information', {
            'fields': (
                'name',
                ('meta_title', 'meta_description'),
                'slug'
            ),
            'description': 'Enter the basic information about the service. The meta title and description are important for SEO.',
            'classes': ('wide',)
        }),
        ('2. Hero Section', {
            'fields': (
                'hero_title',
                'hero_subtitle',
                ('hero_image', 'preview_hero_image'),
                'hero_rating'
            ),
            'description': 'Configure the hero section that appears at the top of the service page.',
            'classes': ('wide',)
        }),
        ('3. Service Stats Section', {
            'fields': (
                'stats_title',
                'stats_subtitle',
                'stats_bottom_paragraph'
            ),
            'description': 'Configure the statistics section that highlights key service metrics.',
            'classes': ('wide',)
        }),
        ('4. Features Section', {
            'fields': (
                'features_title',
                'features_subtitle',
                'features_bottom_paragraph'
            ),
            'description': 'Set the title and subtitle for the features section.',
            'classes': ('wide',)
        }),
        ('5. Specialized Services Section', {
            'fields': (
                'specialized_services_title',
                'specialized_services_subtitle',
                'specialized_services_bottom_paragraph'
            ),
            'description': 'Configure the specialized services section.',
            'classes': ('wide',)
        }),
        ('6. Types of Services Section', {
            'fields': (
                'service_types_title',
                'service_types_subtitle',
                'service_types_bottom_paragraph'
            ),
            'description': 'Set the title and subtitle for the types of services section.',
            'classes': ('wide',)
        }),
        ('7. Benefits Section', {
            'fields': (
                'benefits_title',
                'benefits_subtitle',
                ('benefits_link_text', 'benefits_link_url'),
                'benefits_bottom_paragraph'
            ),
            'description': 'Configure the benefits section and its call-to-action link.',
            'classes': ('wide',)
        }),
        ('8. Choose Right Service Section', {
            'fields': (
                'choose_service_title',
                'choose_service_subtitle',
                ('choose_service_image', 'preview_choose_service_image'),
                'choose_service_bottom_paragraph'
            ),
            'description': 'Configure the section that helps users choose the right service.',
            'classes': ('wide',)
        }),
        ('9. Why Hire Us Section', {
            'fields': (
                'why_hire_title',
                'why_hire_subtitle',
                ('why_hire_image', 'preview_why_hire_image'),
                'why_hire_bottom_paragraph'
            ),
            'description': 'Configure the section that explains why users should choose your service.',
            'classes': ('wide',)
        }),
        ('10. Ideal For Section', {
            'fields': (
                'ideal_for_title',
                'ideal_for_subtitle',
                'ideal_for_bottom_paragraph'
            ),
            'description': 'Set the title and subtitle for the ideal customer section.',
            'classes': ('wide',)
        }),
        ('11. How to Book Section', {
            'fields': (
                'how_to_book_title',
                'how_to_book_subtitle',
                'how_to_book_bottom_paragraph'
            ),
            'description': 'Configure the booking process section.',
            'classes': ('wide',)
        }),
        ('12. Key Considerations Section', {
            'fields': (
                'considerations_title',
                'considerations_subtitle',
                'considerations_bottom_paragraph'
            ),
            'description': 'Set the title and subtitle for the considerations section.',
            'classes': ('wide',)
        }),
        ('13. Hyperlinks Section', {
            'fields': (
                'hyperlinks_title',
                'hyperlinks_subtitle'
            ),
            'description': 'Configure the related services and resources section.',
            'classes': ('wide',)
        }),
        ('14. CTA Section', {
            'fields': (
                'cta_title',
                'cta_subtitle',
                'cta_button_text',
                'cta_secondary_button_text',
                'cta_bottom_paragraph'
            ),
            'description': 'Configure the call-to-action section.',
            'classes': ('wide',)
        }),
        ('15. Lead Form Section', {
            'fields': (
                'lead_form_title',
                'lead_form_subtitle',
                ('lead_form_image', 'preview_lead_form_image')
            ),
            'description': 'Configure the contact form section.',
            'classes': ('wide',)
        }),
        ('16. FAQs Section', {
            'fields': (
                'faqs_title',
                'faqs_subtitle'
            ),
            'description': 'Set the title and subtitle for the FAQs section.',
            'classes': ('wide',)
        }),
        ('17. System Fields', {
            'fields': (
                'created_at',
                'updated_at'
            ),
            'description': 'These fields are automatically managed by the system.',
            'classes': ('collapse',)
        }),
    )
    
    inlines = [
        CustomServiceStatInline,
        CustomServiceFeatureInline,
        HowItWorksStepInline,
        BenefitInline,
        SpecializedServiceDetailInline,
        ConsiderationPointInline,
        CustomFAQInline,
        ServiceTypeCardInline,
        IdealForCardInline,
        BookingStepInline,
        HyperlinkCardInline,
        SpecializedServiceCardInline,
    ]

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'service', 'truncated_description')
    list_filter = ('service',)
    search_fields = ('title', 'description', 'service__name')
    raw_id_fields = ('service',)

    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> {}', obj.icon, obj.icon)
    icon_preview.short_description = "Icon"

    def truncated_description(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    truncated_description.short_description = "Description"

@admin.register(ServiceStat)
class ServiceStatAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'service', 'truncated_description')
    list_filter = ('service',)
    search_fields = ('title', 'description', 'service__name')
    raw_id_fields = ('service',)

    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> {}', obj.icon, obj.icon)
    icon_preview.short_description = "Icon"

    def truncated_description(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    truncated_description.short_description = "Description"

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'truncated_answer')
    list_filter = ('service',)
    search_fields = ('question', 'answer', 'service__name')
    raw_id_fields = ('service',)

    def truncated_answer(self, obj):
        return obj.answer[:100] + '...' if len(obj.answer) > 100 else obj.answer
    truncated_answer.short_description = "Answer"

@admin.register(HowItWorksStep)
class HowItWorksStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'service')
    list_filter = ('service',)
    search_fields = ('title', 'description', 'service__name')
    ordering = ['service', 'step_number']

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'service')
    list_filter = ('service',)
    search_fields = ('title', 'description', 'service__name')

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<i class="{}"></i> {}', obj.icon, obj.icon)
        return "-"
    icon_preview.short_description = "Icon"

@admin.register(SpecializedServiceDetail)
class SpecializedServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'service')
    list_filter = ('service',)
    search_fields = ('title', 'description', 'service__name')

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<i class="{}"></i> {}', obj.icon, obj.icon)
        return "-"
    icon_preview.short_description = "Icon"

@admin.register(ConsiderationPoint)
class ConsiderationPointAdmin(admin.ModelAdmin):
    list_display = ('truncated_point', 'icon_preview', 'service')
    list_filter = ('service',)
    search_fields = ('point_text', 'service__name')

    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> {}', obj.icon, obj.icon)
    icon_preview.short_description = "Icon"

    def truncated_point(self, obj):
        return obj.point_text[:100] + '...' if len(obj.point_text) > 100 else obj.point_text
    truncated_point.short_description = "Point"

# Simple admin interfaces for remaining models
admin.site.register(Lead)
admin.site.register(Blog)
admin.site.register(Services)
