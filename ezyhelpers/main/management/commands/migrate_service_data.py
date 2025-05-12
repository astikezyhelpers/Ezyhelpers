"""
Data migration script to preserve relationships between MainService and its related models.

This script should be run before applying the schema migration that removes the M2M fields.
You can run this manually or incorporate it into a Django migration using RunPython.

Instructions:
1. Save this as a standalone Python script in the project folder
2. Run it using: python manage.py shell < data_migration_script.py
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from main.models import MainService, ServiceStat, ServiceFeature, FAQ

class Command(BaseCommand):
    help = 'Migrates data from M2M relationships to FK relationships for MainService'

    def handle(self, *args, **options):
        self.stdout.write('Starting data migration for MainService relationships...')
        
        try:
            with transaction.atomic():
                # Get all MainService instances
                services = MainService.objects.all()
                self.stdout.write(f'Found {len(services)} MainService instances to process')
                
                # Process each MainService
                for service in services:
                    # Process stats
                    for stat in service.stats.all():
                        new_stat = ServiceStat.objects.create(
                            service=service,
                            title=stat.title,
                            icon=stat.icon,
                            description=stat.description
                        )
                        self.stdout.write(f'Created new ServiceStat "{new_stat.title}" for service "{service.name}"')
                    
                    # Process features
                    for feature in service.features.all():
                        new_feature = ServiceFeature.objects.create(
                            service=service,
                            title=feature.title,
                            icon=feature.icon,
                            description=feature.description
                        )
                        self.stdout.write(f'Created new ServiceFeature "{new_feature.title}" for service "{service.name}"')
                    
                    # Process FAQs
                    for faq in service.faqs.all():
                        new_faq = FAQ.objects.create(
                            service=service,
                            question=faq.question,
                            answer=faq.answer
                        )
                        self.stdout.write(f'Created new FAQ "{new_faq.question}" for service "{service.name}"')
            
            self.stdout.write(self.style.SUCCESS('Data migration completed successfully!'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during migration: {str(e)}'))
            raise 