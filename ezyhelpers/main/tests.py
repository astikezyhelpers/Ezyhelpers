from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import MainService

class MainServiceModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        # Create a complete service with all required fields
        self.complete_service = MainService.objects.create(
            name="Test Service",
            meta_title="Test Meta Title",
            meta_description="Test Meta Description",
            
            # Hero Section
            hero_title="Test Hero Title",
            hero_subtitle="Test Hero Subtitle",
            hero_image="static/service_images/test.jpg",
            
            # Service Stats Section
            stats_title="Test Stats Title",
            stats_subtitle="Test Stats Subtitle",
            
            # Features Section
            features_title="Test Features Title",
            features_subtitle="Test Features Subtitle",
            
            # How to Book Section
            how_to_book_title="Test How to Book Title",
            how_to_book_subtitle="Test How to Book Subtitle",
            
            # Key Considerations Section
            considerations_title="Test Considerations Title",
            considerations_subtitle="Test Considerations Subtitle",
            
            # Hyperlinks Section
            hyperlinks_title="Test Hyperlinks Title",
            hyperlinks_subtitle="Test Hyperlinks Subtitle",
            
            # CTA Section
            cta_title="Test CTA Title",
            cta_subtitle="Test CTA Subtitle",
            cta_button_text="Test Button",
            cta_secondary_button_text="Test Secondary Button",
            
            # Lead Form Section
            lead_form_title="Test Lead Form Title",
            lead_form_subtitle="Test Lead Form Subtitle",
            
            # FAQs Section
            faqs_title="Test FAQs Title",
            faqs_subtitle="Test FAQs Subtitle"
        )

    def test_required_sections_complete(self):
        """Test that a service with all required sections is valid"""
        required_sections = self.complete_service.check_required_sections()
        self.assertTrue(all(required_sections.values()))

    def test_optional_sections_can_be_empty(self):
        """Test that optional sections can be left empty"""
        # Create a service with only required fields
        minimal_service = MainService.objects.create(
            name="Minimal Service",
            meta_title="Minimal Meta Title",
            meta_description="Minimal Meta Description",
            
            # Hero Section
            hero_title="Minimal Hero Title",
            hero_subtitle="Minimal Hero Subtitle",
            hero_image="static/service_images/minimal.jpg",
            
            # Service Stats Section
            stats_title="Minimal Stats Title",
            stats_subtitle="Minimal Stats Subtitle",
            
            # Features Section
            features_title="Minimal Features Title",
            features_subtitle="Minimal Features Subtitle",
            
            # How to Book Section
            how_to_book_title="Minimal How to Book Title",
            how_to_book_subtitle="Minimal How to Book Subtitle",
            
            # Key Considerations Section
            considerations_title="Minimal Considerations Title",
            considerations_subtitle="Minimal Considerations Subtitle",
            
            # Hyperlinks Section
            hyperlinks_title="Minimal Hyperlinks Title",
            hyperlinks_subtitle="Minimal Hyperlinks Subtitle",
            
            # CTA Section
            cta_title="Minimal CTA Title",
            cta_subtitle="Minimal CTA Subtitle",
            cta_button_text="Minimal Button",
            cta_secondary_button_text="Minimal Secondary Button",
            
            # Lead Form Section
            lead_form_title="Minimal Lead Form Title",
            lead_form_subtitle="Minimal Lead Form Subtitle",
            
            # FAQs Section
            faqs_title="Minimal FAQs Title",
            faqs_subtitle="Minimal FAQs Subtitle"
        )
        
        # Verify that optional sections can be empty
        self.assertIsNone(minimal_service.specialized_services_title)
        self.assertIsNone(minimal_service.service_types_title)
        self.assertIsNone(minimal_service.benefits_title)
        self.assertIsNone(minimal_service.choose_service_title)
        self.assertIsNone(minimal_service.why_hire_title)
        self.assertIsNone(minimal_service.ideal_for_title)

    def test_missing_required_sections(self):
        """Test that missing required sections are detected"""
        # Create a service missing some required fields
        incomplete_service = MainService.objects.create(
            name="Incomplete Service",
            meta_title="Incomplete Meta Title",
            meta_description="Incomplete Meta Description",
            
            # Hero Section
            hero_title="Incomplete Hero Title",
            hero_subtitle="Incomplete Hero Subtitle",
            hero_image="static/service_images/incomplete.jpg",
            
            # Service Stats Section
            stats_title="Incomplete Stats Title",
            # Missing stats_subtitle
            
            # Features Section
            features_title="Incomplete Features Title",
            features_subtitle="Incomplete Features Subtitle",
            
            # How to Book Section
            how_to_book_title="Incomplete How to Book Title",
            how_to_book_subtitle="Incomplete How to Book Subtitle",
            
            # Key Considerations Section
            considerations_title="Incomplete Considerations Title",
            considerations_subtitle="Incomplete Considerations Subtitle",
            
            # Hyperlinks Section
            hyperlinks_title="Incomplete Hyperlinks Title",
            hyperlinks_subtitle="Incomplete Hyperlinks Subtitle",
            
            # CTA Section
            cta_title="Incomplete CTA Title",
            cta_subtitle="Incomplete CTA Subtitle",
            cta_button_text="Incomplete Button",
            cta_secondary_button_text="Incomplete Secondary Button",
            
            # Lead Form Section
            lead_form_title="Incomplete Lead Form Title",
            lead_form_subtitle="Incomplete Lead Form Subtitle",
            
            # FAQs Section
            faqs_title="Incomplete FAQs Title",
            faqs_subtitle="Incomplete FAQs Subtitle"
        )
        
        required_sections = incomplete_service.check_required_sections()
        self.assertFalse(all(required_sections.values()))
        self.assertFalse(required_sections['Service Stats Section'])

    def test_slug_generation(self):
        """Test that slugs are automatically generated"""
        service = MainService.objects.create(
            name="Test Service Name",
            meta_title="Test Meta Title",
            meta_description="Test Meta Description",
            
            # Hero Section
            hero_title="Test Hero Title",
            hero_subtitle="Test Hero Subtitle",
            hero_image="static/service_images/test.jpg",
            
            # Service Stats Section
            stats_title="Test Stats Title",
            stats_subtitle="Test Stats Subtitle",
            
            # Features Section
            features_title="Test Features Title",
            features_subtitle="Test Features Subtitle",
            
            # How to Book Section
            how_to_book_title="Test How to Book Title",
            how_to_book_subtitle="Test How to Book Subtitle",
            
            # Key Considerations Section
            considerations_title="Test Considerations Title",
            considerations_subtitle="Test Considerations Subtitle",
            
            # Hyperlinks Section
            hyperlinks_title="Test Hyperlinks Title",
            hyperlinks_subtitle="Test Hyperlinks Subtitle",
            
            # CTA Section
            cta_title="Test CTA Title",
            cta_subtitle="Test CTA Subtitle",
            cta_button_text="Test Button",
            cta_secondary_button_text="Test Secondary Button",
            
            # Lead Form Section
            lead_form_title="Test Lead Form Title",
            lead_form_subtitle="Test Lead Form Subtitle",
            
            # FAQs Section
            faqs_title="Test FAQs Title",
            faqs_subtitle="Test FAQs Subtitle"
        )
        
        self.assertEqual(service.slug, "test-service-name")

    def test_unique_slug(self):
        """Test that duplicate slugs are not allowed"""
        # Create first service
        MainService.objects.create(
            name="Test Service",
            meta_title="Test Meta Title",
            meta_description="Test Meta Description",
            
            # Hero Section
            hero_title="Test Hero Title",
            hero_subtitle="Test Hero Subtitle",
            hero_image="static/service_images/test.jpg",
            
            # Service Stats Section
            stats_title="Test Stats Title",
            stats_subtitle="Test Stats Subtitle",
            
            # Features Section
            features_title="Test Features Title",
            features_subtitle="Test Features Subtitle",
            
            # How to Book Section
            how_to_book_title="Test How to Book Title",
            how_to_book_subtitle="Test How to Book Subtitle",
            
            # Key Considerations Section
            considerations_title="Test Considerations Title",
            considerations_subtitle="Test Considerations Subtitle",
            
            # Hyperlinks Section
            hyperlinks_title="Test Hyperlinks Title",
            hyperlinks_subtitle="Test Hyperlinks Subtitle",
            
            # CTA Section
            cta_title="Test CTA Title",
            cta_subtitle="Test CTA Subtitle",
            cta_button_text="Test Button",
            cta_secondary_button_text="Test Secondary Button",
            
            # Lead Form Section
            lead_form_title="Test Lead Form Title",
            lead_form_subtitle="Test Lead Form Subtitle",
            
            # FAQs Section
            faqs_title="Test FAQs Title",
            faqs_subtitle="Test FAQs Subtitle"
        )
        
        # Try to create second service with same name
        with self.assertRaises(Exception):
            MainService.objects.create(
                name="Test Service",
                meta_title="Test Meta Title 2",
                meta_description="Test Meta Description 2",
                
                # Hero Section
                hero_title="Test Hero Title 2",
                hero_subtitle="Test Hero Subtitle 2",
                hero_image="static/service_images/test2.jpg",
                
                # Service Stats Section
                stats_title="Test Stats Title 2",
                stats_subtitle="Test Stats Subtitle 2",
                
                # Features Section
                features_title="Test Features Title 2",
                features_subtitle="Test Features Subtitle 2",
                
                # How to Book Section
                how_to_book_title="Test How to Book Title 2",
                how_to_book_subtitle="Test How to Book Subtitle 2",
                
                # Key Considerations Section
                considerations_title="Test Considerations Title 2",
                considerations_subtitle="Test Considerations Subtitle 2",
                
                # Hyperlinks Section
                hyperlinks_title="Test Hyperlinks Title 2",
                hyperlinks_subtitle="Test Hyperlinks Subtitle 2",
                
                # CTA Section
                cta_title="Test CTA Title 2",
                cta_subtitle="Test CTA Subtitle 2",
                cta_button_text="Test Button 2",
                cta_secondary_button_text="Test Secondary Button 2",
                
                # Lead Form Section
                lead_form_title="Test Lead Form Title 2",
                lead_form_subtitle="Test Lead Form Subtitle 2",
                
                # FAQs Section
                faqs_title="Test FAQs Title 2",
                faqs_subtitle="Test FAQs Subtitle 2"
            )
