from django.db import migrations, models
import django.db.models.deletion

def migrate_m2m_to_fk(apps, schema_editor):
    """
    This function migrates the data from Many-to-Many relationships to 
    ForeignKey relationships for MainService related models.
    """
    MainService = apps.get_model('main', 'MainService')
    ServiceStat = apps.get_model('main', 'ServiceStat')
    ServiceFeature = apps.get_model('main', 'ServiceFeature')
    FAQ = apps.get_model('main', 'FAQ')
    
    # Get all MainService instances
    services = MainService.objects.all()
    
    # Process each MainService
    for service in services:
        # Process stats
        for stat in service.stats.all():
            # Create a copy of the stat specifically for this service
            ServiceStat.objects.create(
                service=service,
                title=stat.title,
                icon=stat.icon,
                description=stat.description
            )
        
        # Process features
        for feature in service.features.all():
            # Create a copy of the feature specifically for this service
            ServiceFeature.objects.create(
                service=service,
                title=feature.title,
                icon=feature.icon,
                description=feature.description
            )
        
        # Process FAQs
        for faq in service.faqs.all():
            # Create a copy of the FAQ specifically for this service
            FAQ.objects.create(
                service=service,
                question=faq.question,
                answer=faq.answer
            )

def reverse_migrate_m2m_to_fk(apps, schema_editor):
    """
    This function reverses the migration by copying data back to M2M relationships
    """
    MainService = apps.get_model('main', 'MainService')
    ServiceStat = apps.get_model('main', 'ServiceStat')
    ServiceFeature = apps.get_model('main', 'ServiceFeature')
    FAQ = apps.get_model('main', 'FAQ')
    
    # Process each MainService
    for service in MainService.objects.all():
        # Process stats
        for stat in ServiceStat.objects.filter(service=service):
            service.stats.add(stat)
        
        # Process features
        for feature in ServiceFeature.objects.filter(service=service):
            service.features.add(feature)
        
        # Process FAQs
        for faq in FAQ.objects.filter(service=service):
            service.faqs.add(faq)

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        # Add ForeignKey fields to ServiceStat, ServiceFeature, and FAQ
        migrations.AddField(
            model_name='servicestat',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_stats', to='main.mainservice'),
        ),
        migrations.AddField(
            model_name='servicefeature',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_features', to='main.mainservice'),
        ),
        migrations.AddField(
            model_name='faq',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_faqs', to='main.mainservice'),
        ),
        
        # Run the data migration to preserve existing relationships
        migrations.RunPython(
            migrate_m2m_to_fk,
            reverse_migrate_m2m_to_fk
        ),
        
        # Remove M2M fields from MainService after data has been migrated
        migrations.RemoveField(
            model_name='mainservice',
            name='stats',
        ),
        migrations.RemoveField(
            model_name='mainservice',
            name='features',
        ),
        migrations.RemoveField(
            model_name='mainservice',
            name='faqs',
        ),
    ] 