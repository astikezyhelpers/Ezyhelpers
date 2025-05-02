from django.contrib import admin
from .models import (
    Blog, Services, MainService, ServiceFeature, ServiceStat, FAQ, HowItWorksStep,
    Benefit, SpecializedServiceDetail, ConsiderationPoint, Lead
)
from django.utils.text import slugify

class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    search_fields = ('title', 'description')

class ServiceStatAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    search_fields = ('title', 'description')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question', 'answer')

# Inline Admin for How It Works Steps
class HowItWorksStepInline(admin.TabularInline):
    model = HowItWorksStep
    extra = 1 # Number of empty forms to display
    fields = ('step_number', 'title', 'icon', 'description')
    # You might want to customize the widget for description if needed

# Inline Admin for Benefits
class BenefitInline(admin.TabularInline):
    model = Benefit
    extra = 1
    fields = ('title', 'icon', 'description')

# Inline Admin for Specialized Service Details
class SpecializedServiceDetailInline(admin.TabularInline):
    model = SpecializedServiceDetail
    extra = 1
    fields = ('title', 'icon', 'description')

# Inline Admin for Consideration Points
class ConsiderationPointInline(admin.TabularInline):
    model = ConsiderationPoint
    extra = 1
    fields = ('icon', 'point_text')

class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'meta_title', 'meta_description')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('stats', 'features', 'faqs')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'meta_title', 'meta_description')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image', 'hero_rating'),
            'classes': ('collapse',),
        }),
        ('Stats & Features', {
            'fields': ('stats', 'features', 'features_title'),
            'classes': ('collapse',),
        }),
        ('How It Works', {
            'fields': ('how_it_works_title',),
            'classes': ('collapse',),
            # Steps will be managed by the inline below
        }),
        ('Benefits', {
            'fields': ('benefits_title', 'benefits_link_text', 'benefits_link_url'),
            'classes': ('collapse',),
        }),
        ('Specialized Services', {
            'fields': ('specialized_services_title',),
            'classes': ('collapse',),
        }),
        ('Considerations', {
            'fields': ('considerations_title',),
            'classes': ('collapse',),
        }),
        ('FAQs', {
            'fields': ('faqs',),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    inlines = [
        HowItWorksStepInline,
        BenefitInline,
        SpecializedServiceDetailInline,
        ConsiderationPointInline
    ]

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

admin.site.register(ServiceFeature, ServiceFeatureAdmin)
admin.site.register(ServiceStat, ServiceStatAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(HowItWorksStep)
admin.site.register(Benefit)
admin.site.register(SpecializedServiceDetail)
admin.site.register(ConsiderationPoint)
admin.site.register(Lead)
admin.site.register(MainService, MainServiceAdmin)
admin.site.register(Blog)
admin.site.register(Services)
