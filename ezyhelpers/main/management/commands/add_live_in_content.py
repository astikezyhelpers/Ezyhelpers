from django.core.management.base import BaseCommand
from main.models import ServiceStat, ServiceFeature, FAQ, MainService, HowItWorksStep, Benefit, SpecializedServiceDetail, ConsiderationPoint

# Note: Full FAQ answers are truncated below for brevity in the edit.
# Ensure the full HTML is present in your actual implementation if needed.

class Command(BaseCommand):
    help = 'Populates the database with initial content for the Live-in Helper service. Clears existing data for this service first.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Attempting to clear existing Live-in Helper data...'))

        # Find the service instance if it exists
        live_in_service = MainService.objects.filter(slug='live-in-helpers').first()

        if live_in_service:
            # Clear related objects first (using the instance)
            HowItWorksStep.objects.filter(service=live_in_service).delete()
            Benefit.objects.filter(service=live_in_service).delete()
            SpecializedServiceDetail.objects.filter(service=live_in_service).delete()
            ConsiderationPoint.objects.filter(service=live_in_service).delete()
            # M2M fields are cleared automatically when the service is deleted
            live_in_service.delete()
            self.stdout.write(self.style.SUCCESS('Existing Live-in Helper data cleared.'))
        else:
            self.stdout.write(self.style.NOTICE('No existing Live-in Helper data found to clear.'))

        self.stdout.write('Adding new Live-in Helper data...')

        # --- Get or Create Stats ---
        # Using get_or_create to avoid duplicates if run multiple times or if stats are shared
        stat1, _ = ServiceStat.objects.get_or_create(
            title="Thoroughly Vetted",
            defaults={'icon': "fas fa-user-shield", 'description': "5-step screening process including background checks and reference verification"}
        )
        stat2, _ = ServiceStat.objects.get_or_create(
            title="Trained Professionals",
            defaults={'icon': "fas fa-certificate", 'description': "Minimum 100 hours of training in household management and care"}
        )
        stat3, _ = ServiceStat.objects.get_or_create(
            title="Quick Placement",
            defaults={'icon': "fas fa-history", 'description': "Average placement time of just 7 days from initial consultation"}
        )
        stat4, _ = ServiceStat.objects.get_or_create(
            title="24/7 Support",
            defaults={'icon': "fas fa-headset", 'description': "Dedicated support team available anytime you need assistance"}
        )
        stats = [stat1, stat2, stat3, stat4]

        # --- Get or Create Features ---
        feature1, _ = ServiceFeature.objects.get_or_create(
            title="Housekeeping & Deep Cleaning",
            defaults={'icon': "fas fa-broom", 'description': "Maintain a spotless home with regular sweeping, mopping, dusting, and deep cleaning services. Laundry and ironing are also handled with care, ensuring your home stays fresh and organized."}
        )
        feature2, _ = ServiceFeature.objects.get_or_create(
            title="Cooking & Meal Preparation",
            defaults={'icon': "fas fa-utensils", 'description': "Enjoy nutritious meals tailored to your dietary preferences. Our professionals handle everything from grocery shopping and meal planning to cooking and post-meal cleanup, making your daily routine hassle-free."}
        )
        feature3, _ = ServiceFeature.objects.get_or_create(
            title="Child Care Assistance",
            defaults={'icon': "fas fa-baby", 'description': "Our experienced caregivers provide babysitting services, engage children in creative activities, and offer homework help. School pickup and drop-off, along with extracurricular coordination, ensure a smooth daily routine for your little ones."}
        )
        feature4, _ = ServiceFeature.objects.get_or_create(
            title="Elderly Care Support",
            defaults={'icon': "fas fa-user-nurse", 'description': "Provide your elderly ones with companionship and emotional support. Our trained caregivers assist with personal care needs such as bathing and grooming while also managing medications and accompanying seniors on doctor visits."}
        )
        features = [feature1, feature2, feature3, feature4]

        # --- Get or Create FAQs ---
        faq1_answer = """<p>Our one-time placement fee includes:</p>...""" # Full answer here
        faq2_answer = """<p>Standard arrangements include:</p>...""" # Full answer here
        faq3_answer = """<p>We recommend including these provisions in your contract:</p>...""" # Full answer here

        faq1, _ = FAQ.objects.get_or_create(question="What's included in the placement fee?", defaults={'answer': faq1_answer})
        faq2, _ = FAQ.objects.get_or_create(question="What are the typical working hours for a live-in helper?", defaults={'answer': faq2_answer})
        faq3, _ = FAQ.objects.get_or_create(question="What if my helper gets sick or needs time off?", defaults={'answer': faq3_answer})
        faqs = [faq1, faq2, faq3]

        # --- Create Main Service ---
        # Since we deleted it earlier, we use create here.
        service = MainService.objects.create(
            name="Live-In Maid",
            slug="live-in-helpers",
            meta_title="EzyHelpers - Professional Live-In Maid Services in Bangalore | 24x7 Help",
            meta_description="Get reliable 24x7 live-in maid services in Bangalore...", # Truncated
            hero_title='<span class="text-primary">Live-In Maid</span> Bangalore: Get 24x7 Household Help',
            hero_subtitle="Feeling overwhelmed by household chaos?...", # Truncated
            hero_rating=4.98,
            features_title="Services Offered by Our Live-In Maids in Bangalore",
            how_it_works_title="How Our Live-in Helper Service Works",
            benefits_title="Benefits of Hiring a Live-in Maid Through EzyHelpers",
            benefits_link_text="Full-Time Maids in Bangalore",
            benefits_link_url="/services/full-time-helpers",
            specialized_services_title="We also provide specialised live-in services for:",
            considerations_title="Key Factors to Consider Before Hiring a 24/7 Maid",
            # Add hero_image assignment here if necessary
        )

        # --- Create How It Works Steps --- 
        HowItWorksStep.objects.create(service=service, step_number=1, title="Consultation", description="<p>We discuss your needs, preferences, and household requirements.</p>")
        HowItWorksStep.objects.create(service=service, step_number=2, title="Matching", description="<p>We select 2-3 pre-screened candidates that match your criteria.</p>")
        HowItWorksStep.objects.create(service=service, step_number=3, title="Interviews", description="<p>Meet the candidates (in-person or virtually) with our guidance.</p>")
        HowItWorksStep.objects.create(service=service, step_number=4, title="Onboarding", description="<p>Your helper starts, with our ongoing support ensuring smooth transition.</p>")

        # --- Create Benefits ---
        Benefit.objects.create(service=service, title="24/7 Support", icon="fas fa-headset", description="<p>Get round-the-clock live-in maid support...</p>") # Truncated
        Benefit.objects.create(service=service, title="Personalized Care", icon="fas fa-heart", description="<p>Our background-checked, stay-at-home maids adapt...</p>") # Truncated
        Benefit.objects.create(service=service, title="Enhanced Security", icon="fas fa-shield-alt", description="<p>Improve home security with a trusted presence...</p>") # Truncated
        Benefit.objects.create(service=service, title="Stress-Free Home", icon="fas fa-home", description="<p>Perfect for busy families and professionals...</p>") # Truncated

        # --- Create Specialized Service Details ---
        SpecializedServiceDetail.objects.create(service=service, title="Live-In Nanny/Babysitters", icon="fas fa-baby-carriage", description="<p>Expert childcare for infants and kids.</p>")
        SpecializedServiceDetail.objects.create(service=service, title="Live-In Elderly Home Attendants", icon="fas fa-user-nurse", description="<p>Compassionate elderly care at home.</p>")
        SpecializedServiceDetail.objects.create(service=service, title="Live-In Cooks", icon="fas fa-utensils", description="<p>Personalised, home-cooked meals daily.</p>")
        SpecializedServiceDetail.objects.create(service=service, title="Live-In Drivers", icon="fas fa-car", description="<p>Reliable transportation for work, school, and travel.</p>")

        # --- Create Consideration Points ---
        ConsiderationPoint.objects.create(service=service, icon="fas fa-user-secret", point_text="<p><strong>Privacy:</strong> Both the employer and the helper...</p>") # Truncated
        ConsiderationPoint.objects.create(service=service, icon="fas fa-bed", point_text="<p><strong>Living Arrangements:</strong> Adequate, private living space...</p>") # Truncated
        ConsiderationPoint.objects.create(service=service, icon="fas fa-balance-scale", point_text="<p><strong>Legal & Ethical Considerations:</strong> Employment terms must comply...</p>") # Truncated

        # Add M2M relationships
        service.stats.set(stats)
        service.features.set(features)
        service.faqs.set(faqs)

        self.stdout.write(self.style.SUCCESS('Successfully added Live-in Helper content.')) 