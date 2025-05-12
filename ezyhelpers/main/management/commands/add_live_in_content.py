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
            ServiceStat.objects.filter(service=live_in_service).delete()
            ServiceFeature.objects.filter(service=live_in_service).delete()
            FAQ.objects.filter(service=live_in_service).delete()
            HowItWorksStep.objects.filter(service=live_in_service).delete()
            Benefit.objects.filter(service=live_in_service).delete()
            SpecializedServiceDetail.objects.filter(service=live_in_service).delete()
            ConsiderationPoint.objects.filter(service=live_in_service).delete()
            live_in_service.delete()
            self.stdout.write(self.style.SUCCESS('Existing Live-in Helper data cleared.'))
        else:
            self.stdout.write(self.style.NOTICE('No existing Live-in Helper data found to clear.'))

        self.stdout.write('Adding new Live-in Helper data...')

        # Create Main Service
        service = MainService.objects.create(
            name="Live-In Maid",
            slug="live-in-helpers",
            meta_title="EzyHelpers - Professional Live-In Maid Services in Bangalore | 24x7 Help",
            meta_description="Get reliable 24x7 live-in maid services in Bangalore. Our thoroughly vetted and trained live-in maids provide comprehensive household help including cooking, cleaning, and childcare. Book your live-in helper today!",
            hero_title='<span class="text-primary">Live-In Maid</span> Bangalore: Get 24x7 Household Help',
            hero_subtitle="Feeling overwhelmed by household chaos? Our live-in maids provide round-the-clock support for all your domestic needs. From cooking and cleaning to childcare, get reliable, vetted help that stays with you.",
            hero_rating=4.98,
            features_title="Services Offered by Our Live-In Maids in Bangalore",
            how_it_works_title="How Our Live-in Helper Service Works",
            benefits_title="Benefits of Hiring a Live-in Maid Through EzyHelpers",
            benefits_link_text="Full-Time Maids in Bangalore",
            benefits_link_url="/services/full-time-helpers",
            specialized_services_title="We also provide specialised live-in services for:",
            considerations_title="Key Factors to Consider Before Hiring a 24/7 Maid"
        )

        # Create Stats
        stats_data = [
            {
                'title': "Thoroughly Vetted",
                'icon': "fas fa-user-shield",
                'description': "5-step screening process including background checks and reference verification"
            },
            {
                'title': "Trained Professionals",
                'icon': "fas fa-certificate",
                'description': "Minimum 100 hours of training in household management and care"
            },
            {
                'title': "Quick Placement",
                'icon': "fas fa-history",
                'description': "Average placement time of just 7 days from initial consultation"
            },
            {
                'title': "24/7 Support",
                'icon': "fas fa-headset",
                'description': "Dedicated support team available anytime you need assistance"
            },
            {
                'title': "Satisfaction Guaranteed",
                'icon': "fas fa-heart",
                'description': "98% client satisfaction rate with our live-in maid services"
            },
            {
                'title': "Flexible Options",
                'icon': "fas fa-calendar-alt",
                'description': "Customizable service plans to match your specific needs"
            }
        ]

        for stat_data in stats_data:
            ServiceStat.objects.create(service=service, **stat_data)

        # Create Features
        features_data = [
            {
                'title': "Housekeeping & Deep Cleaning",
                'icon': "fas fa-broom",
                'description': "Maintain a spotless home with regular sweeping, mopping, dusting, and deep cleaning services. Laundry and ironing are also handled with care, ensuring your home stays fresh and organized."
            },
            {
                'title': "Cooking & Meal Preparation",
                'icon': "fas fa-utensils",
                'description': "Enjoy nutritious meals tailored to your dietary preferences. Our professionals handle everything from grocery shopping and meal planning to cooking and post-meal cleanup, making your daily routine hassle-free."
            },
            {
                'title': "Child Care Assistance",
                'icon': "fas fa-baby",
                'description': "Our experienced caregivers provide babysitting services, engage children in creative activities, and offer homework help. School pickup and drop-off, along with extracurricular coordination, ensure a smooth daily routine for your little ones."
            },
            {
                'title': "Elderly Care Support",
                'icon': "fas fa-user-nurse",
                'description': "Provide your elderly ones with companionship and emotional support. Our trained caregivers assist with personal care needs such as bathing and grooming while also managing medications and accompanying seniors on doctor visits."
            },
            {
                'title': "Pet Care Services",
                'icon': "fas fa-paw",
                'description': "Keep your furry friends happy with regular feeding, walking, and grooming services. Our helpers can manage pet schedules and maintain their living spaces."
            },
            {
                'title': "Errands & Shopping",
                'icon': "fas fa-shopping-cart",
                'description': "Let our helpers handle your daily errands including grocery shopping, bill payments, and package collection. Stay organized with efficient management of household supplies."
            }
        ]

        for feature_data in features_data:
            ServiceFeature.objects.create(service=service, **feature_data)

        # Create FAQs
        faqs_data = [
            {
                'question': "What's included in the placement fee?",
                'answer': "<p>Our one-time placement fee includes:</p><ul><li>Thorough background verification</li><li>Professional training and orientation</li><li>Contract preparation and documentation</li><li>Replacement guarantee within 3 months</li><li>24/7 support throughout the contract period</li></ul>"
            },
            {
                'question': "What are the typical working hours for a live-in helper?",
                'answer': "<p>Standard arrangements include:</p><ul><li>12-hour workday with breaks</li><li>Weekly off as per mutual agreement</li><li>Festival holidays as discussed</li><li>Emergency availability when needed</li></ul><p>Exact schedules can be customized based on your requirements.</p>"
            },
            {
                'question': "What if my helper gets sick or needs time off?",
                'answer': "<p>We recommend including these provisions in your contract:</p><ul><li>Paid sick leave for genuine illness (with medical certificate)</li><li>Temporary replacement for extended leaves</li><li>Clear communication protocol for emergencies</li><li>Backup support from our team when needed</li></ul>"
            },
            {
                'question': "How are the live-in maids trained?",
                'answer': "<p>Our comprehensive training program includes:</p><ul><li>Professional housekeeping techniques</li><li>Modern cooking methods and kitchen hygiene</li><li>Child and elderly care best practices</li><li>Emergency response and first aid</li><li>Communication and etiquette training</li></ul>"
            },
            {
                'question': "Can I customize the services based on my needs?",
                'answer': "<p>Yes, our services are highly customizable:</p><ul><li>Choose specific areas of focus (cleaning, cooking, childcare, etc.)</li><li>Set preferred schedules and routines</li><li>Specify dietary requirements and preferences</li><li>Request additional training if needed</li></ul>"
            },
            {
                'question': "What happens if I'm not satisfied with the service?",
                'answer': "<p>Our satisfaction guarantee includes:</p><ul><li>Initial trial period of 15 days</li><li>Free replacement within 3 months if needed</li><li>Regular performance reviews</li><li>Dedicated customer support for issue resolution</li></ul>"
            }
        ]

        for faq_data in faqs_data:
            FAQ.objects.create(service=service, **faq_data)

        # Create How It Works Steps
        steps_data = [
            {
                'step_number': 1,
                'title': "Consultation",
                'icon': "fas fa-comments",
                'description': "<p>Schedule a detailed consultation where we discuss your specific needs, preferences, and household requirements. Our experts will help you understand the service options and create a customized plan.</p>"
            },
            {
                'step_number': 2,
                'title': "Matching",
                'icon': "fas fa-user-check",
                'description': "<p>Based on your requirements, we carefully select 2-3 pre-screened candidates who match your criteria. Each candidate undergoes thorough background verification and skill assessment.</p>"
            },
            {
                'step_number': 3,
                'title': "Interviews",
                'icon': "fas fa-handshake",
                'description': "<p>Meet the shortlisted candidates either in-person or virtually. Our team will guide you through the interview process and help you make the best choice for your household.</p>"
            },
            {
                'step_number': 4,
                'title': "Onboarding",
                'icon': "fas fa-home",
                'description': "<p>Once you select your preferred helper, we handle all documentation and conduct a detailed orientation. Your helper starts with a trial period, during which we provide close support to ensure a smooth transition.</p>"
            },
            {
                'step_number': 5,
                'title': "Regular Follow-up",
                'icon': "fas fa-phone-alt",
                'description': "<p>We maintain regular contact through scheduled check-ins to ensure everything is running smoothly. Our support team is always available to address any concerns or requirements.</p>"
            }
        ]

        for step_data in steps_data:
            HowItWorksStep.objects.create(service=service, **step_data)

        # Create Benefits
        benefits_data = [
            {
                'title': "24/7 Support",
                'icon': "fas fa-headset",
                'description': "<p>Get round-the-clock live-in maid support for all your household needs. Our helpers are trained to handle emergencies and provide assistance whenever required.</p>"
            },
            {
                'title': "Personalized Care",
                'icon': "fas fa-heart",
                'description': "<p>Our background-checked, stay-at-home maids adapt to your family's unique needs and preferences, ensuring a comfortable and harmonious living environment.</p>"
            },
            {
                'title': "Enhanced Security",
                'icon': "fas fa-shield-alt",
                'description': "<p>Improve home security with a trusted presence when you're away. Our live-in helpers are trained to handle emergencies and maintain your home's safety.</p>"
            },
            {
                'title': "Stress-Free Home",
                'icon': "fas fa-home",
                'description': "<p>Perfect for busy families and professionals. Enjoy a well-maintained home without the daily stress of managing household tasks and schedules.</p>"
            },
            {
                'title': "Cost-Effective Solution",
                'icon': "fas fa-wallet",
                'description': "<p>Save money compared to hiring multiple service providers. Our live-in maids offer comprehensive services at a competitive monthly rate.</p>"
            },
            {
                'title': "Professional Standards",
                'icon': "fas fa-star",
                'description': "<p>All our helpers are professionally trained and regularly evaluated to maintain high service standards and ensure client satisfaction.</p>"
            }
        ]

        for benefit_data in benefits_data:
            Benefit.objects.create(service=service, **benefit_data)

        # Create Specialized Service Details
        specialized_services_data = [
            {
                'title': "Live-In Nanny/Babysitters",
                'icon': "fas fa-baby-carriage",
                'description': "<p>Expert childcare providers specializing in infant and child development, educational activities, and maintaining daily routines.</p>"
            },
            {
                'title': "Live-In Elderly Home Attendants",
                'icon': "fas fa-user-nurse",
                'description': "<p>Trained caregivers providing compassionate elderly care, medical assistance, and companionship for seniors.</p>"
            },
            {
                'title': "Live-In Cooks",
                'icon': "fas fa-utensils",
                'description': "<p>Professional cooks offering customized meal planning, dietary accommodation, and gourmet cooking services.</p>"
            },
            {
                'title': "Live-In Drivers",
                'icon': "fas fa-car",
                'description': "<p>Experienced chauffeurs providing safe and reliable transportation for all your travel needs.</p>"
            },
            {
                'title': "Live-In Pet Caregivers",
                'icon': "fas fa-paw",
                'description': "<p>Dedicated pet lovers who provide comprehensive care for your furry family members.</p>"
            },
            {
                'title': "Live-In House Managers",
                'icon': "fas fa-tasks",
                'description': "<p>Professional managers who coordinate all aspects of household operations and staff supervision.</p>"
            }
        ]

        for service_data in specialized_services_data:
            SpecializedServiceDetail.objects.create(service=service, **service_data)

        # Create Consideration Points
        consideration_points_data = [
            {
                'icon': "fas fa-user-secret",
                'point_text': "<p><strong>Privacy:</strong> Both the employer and the helper need to respect each other's privacy and personal space. Clear boundaries should be established from day one.</p>"
            },
            {
                'icon': "fas fa-bed",
                'point_text': "<p><strong>Living Arrangements:</strong> Adequate, private living space with basic amenities must be provided for the live-in helper's comfort and well-being.</p>"
            },
            {
                'icon': "fas fa-balance-scale",
                'point_text': "<p><strong>Legal & Ethical Considerations:</strong> Employment terms must comply with local labor laws. Fair working hours, leaves, and compensation should be clearly defined in the contract.</p>"
            },
            {
                'icon': "fas fa-comments",
                'point_text': "<p><strong>Communication:</strong> Establish clear channels of communication and set expectations regarding tasks, schedules, and house rules.</p>"
            },
            {
                'icon': "fas fa-hand-holding-heart",
                'point_text': "<p><strong>Cultural Sensitivity:</strong> Respect cultural differences and dietary preferences. Create an inclusive and comfortable environment for both parties.</p>"
            },
            {
                'icon': "fas fa-file-contract",
                'point_text': "<p><strong>Documentation:</strong> Ensure all necessary documentation, including employment contract, identity verification, and medical records, are properly maintained.</p>"
            }
        ]

        for point_data in consideration_points_data:
            ConsiderationPoint.objects.create(service=service, **point_data)

        self.stdout.write(self.style.SUCCESS('Successfully added Live-in Helper content.')) 