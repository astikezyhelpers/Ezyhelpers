// // Header Scroll Effect
// window.addEventListener('scroll', function() {
//     const header = document.getElementById('header');
//     const backToTop = document.querySelector('.back-to-top');
    
//     if (window.scrollY > 100) {
//         header.classList.add('scrolled');
//     } else {
//         header.classList.remove('scrolled');
//     }
    
//     if (window.scrollY > 500) {
//         backToTop.classList.add('active');
//     } else {
//         backToTop.classList.remove('active');
//     }
// });

// // Back to Top Button
// document.querySelector('.back-to-top').addEventListener('click', function(e) {
//     e.preventDefault();
//     window.scrollTo({
//         top: 0,
//         behavior: 'smooth'
//     });
// });

// FAQ Accordion
const faqQuestions = document.querySelectorAll('.faq-question');
faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
        const item = question.parentNode;
        item.classList.toggle('active');
        
        // Close other open items
        faqQuestions.forEach(q => {
            if (q !== question) {
                q.parentNode.classList.remove('active');
            }
        });
    });
});

// Testimonial Slider
const testimonialDots = document.querySelectorAll('.testimonial-dot');
testimonialDots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        // Remove active class from all dots
        testimonialDots.forEach(d => d.classList.remove('active'));
        // Add active class to clicked dot
        dot.classList.add('active');
        
        // Move track (in a real implementation, you would have multiple testimonial cards)
        const track = document.querySelector('.testimonial-track');
        track.style.transform = `translateX(-${index * 100}%)`;
    });
});

// How It Works Animation
const steps = document.querySelectorAll('.step');
const stepsLineProgress = document.querySelector('.steps-line-progress');

function animateSteps() {
    steps.forEach((step, index) => {
        const stepPosition = step.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;
        
        if (stepPosition < screenPosition) {
            step.classList.add('completed');
            stepsLineProgress.style.width = `${(index + 1) * 25}%`;
            
            if (index === 2) {
                steps[3].classList.add('active');
            }
        }
    });
}

window.addEventListener('scroll', animateSteps);

// Animation on Scroll
const animateElements = document.querySelectorAll('.animate');

function checkAnimation() {
    animateElements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.2;
        
        if (elementPosition < screenPosition) {
            element.classList.add('animated');
        }
    });
}

window.addEventListener('scroll', checkAnimation);
window.addEventListener('load', checkAnimation);

// Pricing Tabs
const pricingTabs = document.querySelectorAll('.pricing-tab');
pricingTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        pricingTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
    });
});