// Initialize AOS animations
AOS.init({
  duration: 800,
  easing: 'ease-in-out',
  once: true,
  offset: 100
});

// Counter animation for stats
const counters = document.querySelectorAll('.counter');
const speed = 200;

counters.forEach(counter => {
  const target = +counter.getAttribute('data-target');
  const count = +counter.innerText;
  const increment = target / speed;
  
  if (count < target) {
    counter.innerText = Math.ceil(count + increment);
    setTimeout(updateCounter, 1);
  } else {
    counter.innerText = target;
  }
  
  function updateCounter() {
    const count = +counter.innerText;
    const increment = target / speed;
    
    if (count < target) {
      counter.innerText = Math.ceil(count + increment);
      setTimeout(updateCounter, 1);
    } else {
      counter.innerText = target;
    }
  }
});

// FAQ accordion functionality
const faqButtons = document.querySelectorAll('footer [aria-expanded]');
faqButtons.forEach(button => {
  button.addEventListener('click', () => {
    const isExpanded = button.getAttribute('aria-expanded') === 'true';
    button.setAttribute('aria-expanded', !isExpanded);
    const answer = button.nextElementSibling;
    answer.classList.toggle('hidden');
  });
});

// Mobile menu toggle
const mobileMenuButton = document.querySelector('.mobile-menu-button');
const mobileMenu = document.querySelector('.mobile-menu');
if (mobileMenuButton && mobileMenu) {
  mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
  });
}