if (window.innerWidth > 768) {
let lastScroll = 0;
const header = document.querySelector('header');
const scrollThreshold = 100; // How much to scroll before hiding header

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;
  
  if (currentScroll <= 0) {
    // At top of page - show header
    header.classList.remove('scrolled-down');
    header.classList.add('scrolled-up');
    return;
  }
  
  if (currentScroll > lastScroll && !header.classList.contains('scrolled-down') && currentScroll > scrollThreshold) {
    // Scrolling down and past threshold - hide header
    header.classList.remove('scrolled-up');
    header.classList.add('scrolled-down');
  } else if (currentScroll < lastScroll && header.classList.contains('scrolled-down')) {
    // Scrolling up - show header
    header.classList.remove('scrolled-down');
    header.classList.add('scrolled-up');
  }
  
  lastScroll = currentScroll;
});
}

 // Mobile menu toggle functionality
 const headerMobileMenuButton = document.getElementById('mobile-menu-button');
 const headerMobileMenuClose = document.getElementById('mobile-menu-close');
 const headerMobileMenu = document.getElementById('mobile-menu');
 
 headerMobileMenuButton.addEventListener('click', () => {
  headerMobileMenu.classList.remove('hidden');
     document.body.style.overflow = 'hidden'; // Prevent scrolling when menu is open
 });
 
 headerMobileMenuClose.addEventListener('click', () => {
     headerMobileMenu.classList.add('hidden');
     document.body.style.overflow = ''; // Re-enable scrolling
 });