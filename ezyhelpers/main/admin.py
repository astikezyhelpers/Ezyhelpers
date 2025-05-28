from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import slugify
from .models import (
    Blog, Services, MainService, ServiceStat, ServiceFeature, FAQ,
    Benefit, SpecializedServiceDetail, ConsiderationPoint,
    ServiceTypeCard, IdealForCard, BookingStep, HyperlinkCard, Lead,
    WhyChooseUsPoint, ChoosingRightPoint
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

class BenefitInline(CustomInlineMixin, admin.StackedInline):
    model = Benefit
    fields = (
        ('title', 'icon'),
        'description'
    )
    verbose_name = "Benefit"
    verbose_name_plural = "5. Benefits"
    help_text = "Add benefits that customers get from your service"

class SpecializedServiceDetailInline(CustomInlineMixin, admin.StackedInline):
    model = SpecializedServiceDetail
    fields = (
        ('title', 'icon'),
        'description'
    )
    verbose_name = "Specialized Service Detail"
    verbose_name_plural = "3. Specialized Service Details"
    help_text = "Add specialized aspects of your service"

class ConsiderationPointInline(CustomInlineMixin, admin.StackedInline):
    model = ConsiderationPoint
    fields = (
        'icon',
        'point_text'
    )
    verbose_name = "Consideration Point"
    verbose_name_plural = "10. Consideration Points"
    help_text = "Add important points to consider about your service"

class CustomFAQInline(CustomInlineMixin, admin.StackedInline):
    model = FAQ
    fields = (
        'question',
        'answer'
    )
    verbose_name = "FAQ"
    verbose_name_plural = "12. FAQs"
    help_text = "Add frequently asked questions and their answers"

class ServiceTypeCardInline(CustomInlineMixin, admin.StackedInline):
    model = ServiceTypeCard
    fields = (
        ('title', 'icon'),
        'description',
        'order'
    )
    verbose_name = "Service Type"
    verbose_name_plural = "4. Service Types"
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
    verbose_name_plural = "8. Ideal For Cards"
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
    verbose_name_plural = "9. Booking Steps"
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

class WhyChooseUsPointInline(CustomInlineMixin, admin.StackedInline):
    model = WhyChooseUsPoint
    fields = (
        ('title', 'icon'),
        'description',
        'order'
    )
    verbose_name = "Why Choose Us Point"
    verbose_name_plural = "7. Why Choose Us Points"
    help_text = "Add points explaining why customers should choose your service"
    ordering = ['order']

class ChoosingRightPointInline(CustomInlineMixin, admin.StackedInline):
    model = ChoosingRightPoint
    fields = (
        ('title', 'icon'),
        'description',
        'order'
    )
    verbose_name = "Choosing Right Point"
    verbose_name_plural = "6. Choosing Right Points"
    help_text = "Add points to help customers choose the right service"
    ordering = ['order']

@admin.register(MainService)
class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_hero_image', 'created_at', 'updated_at', 'display_stats_count', 'display_features_count')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'meta_title', 'meta_description', 'hero_title', 'hero_subtitle')
    readonly_fields = ('created_at', 'updated_at', 'preview_hero_image')
    save_on_top = True  # Add save buttons at the top of the page
    
    def preview_hero_image(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 200px;" />', obj.hero_image.url)
        return "No image"
    preview_hero_image.short_description = "Hero Image Preview"

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
                ('hero_image', 'hero_image_alt_text', 'preview_hero_image'),
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
            'description': 'Configure the statistics section of your service.',
            'classes': ('wide',)
        }),
        ('4. Features Section', {
            'fields': (
                'features_title',
                'features_subtitle',
                'features_bottom_paragraph'
            ),
            'description': 'Configure the features section of your service.',
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
        ('6. Service Types Section', {
            'fields': (
                'service_types_title',
                'service_types_subtitle',
                'service_types_bottom_paragraph'
            ),
            'description': 'Configure the service types section.',
            'classes': ('wide',)
        }),
        ('7. Benefits Section', {
            'fields': (
                'benefits_title',
                'benefits_subtitle',
                'benefits_link_text',
                'benefits_link_url',
                'benefits_bottom_paragraph'
            ),
            'description': 'Configure the benefits section.',
            'classes': ('wide',)
        }),
        ('8. Choose Service Section', {
            'fields': (
                'choose_service_title',
                'choose_service_subtitle',
                ('choose_service_image', 'choose_service_image_alt_text'),
                'choose_service_bottom_paragraph'
            ),
            'description': 'Configure the choose service section.',
            'classes': ('wide',)
        }),
        ('9. Why Hire Us Section', {
            'fields': (
                'why_hire_title',
                'why_hire_subtitle',
                ('why_hire_image', 'why_hire_image_alt_text'),
                'why_hire_bottom_paragraph'
            ),
            'description': 'Configure the why hire us section.',
            'classes': ('wide',)
        }),
        ('10. Ideal For Section', {
            'fields': (
                'ideal_for_title',
                'ideal_for_subtitle',
                'ideal_for_bottom_paragraph'
            ),
            'description': 'Configure the ideal for section.',
            'classes': ('wide',)
        }),
        ('11. How to Book Section', {
            'fields': (
                'how_to_book_title',
                'how_to_book_subtitle',
                'how_to_book_bottom_paragraph'
            ),
            'description': 'Configure the how to book section.',
            'classes': ('wide',)
        }),
        ('12. Considerations Section', {
            'fields': (
                'considerations_title',
                'considerations_subtitle',
                'considerations_bottom_paragraph'
            ),
            'description': 'Configure the considerations section.',
            'classes': ('wide',)
        }),
        ('13. Hyperlinks Section', {
            'fields': (
                'hyperlinks_title',
                'hyperlinks_subtitle'
            ),
            'description': 'Configure the hyperlinks section.',
            'classes': ('wide',)
        }),
        ('14. CTA Section', {
            'fields': (
                'cta_title',
                'cta_subtitle',
                'cta_bottom_paragraph'
            ),
            'description': 'Configure the call-to-action section.',
            'classes': ('wide',)
        }),
        ('15. Lead Form Section', {
            'fields': (
                'lead_form_title',
                'lead_form_subtitle',
                ('lead_form_image', 'lead_form_image_alt_text')
            ),
            'description': 'Configure the lead form section.',
            'classes': ('wide',)
        }),
        ('16. FAQs Section', {
            'fields': (
                'faqs_title',
                'faqs_subtitle'
            ),
            'description': 'Configure the FAQs section.',
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
        # 1. Service Stats Section
        CustomServiceStatInline,
        # 2. Service Features Section
        CustomServiceFeatureInline,
        # 3. Specialized Services Section
        SpecializedServiceDetailInline,
        # 4. Service Types Section
        ServiceTypeCardInline,
        # 5. Benefits Section
        BenefitInline,
        # 6. Choose Service Section
        ChoosingRightPointInline,
        # 7. Why Hire Us Section
        WhyChooseUsPointInline,
        # 8. Ideal For Section
        IdealForCardInline,
        # 9. How to Book Section
        BookingStepInline,
        # 10. Considerations Section
        ConsiderationPointInline,
        # 11. Hyperlinks Section
        HyperlinkCardInline,
        # 12. FAQs Section
        CustomFAQInline,
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

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'reading_time')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}  # This will auto-populate but still allow editing

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'content')
    prepopulated_fields = {'slug': ('name',)}  # This will auto-populate but still allow editing
