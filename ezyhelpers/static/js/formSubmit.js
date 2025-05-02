// Add a check to ensure the element exists before adding listeners
const scrollContainer = document.querySelector('.scrolling-services-container');

if (scrollContainer) {
    // Pause animation on hover for better UX
    scrollContainer.addEventListener('mouseenter', function() {
        const scroller = this.querySelector('.scrolling-services');
        if (scroller) { // Also check if inner element exists
             scroller.style.animationPlayState = 'paused';
        }
    });
    
    scrollContainer.addEventListener('mouseleave', function() {
        const scroller = this.querySelector('.scrolling-services');
        if (scroller) { // Also check if inner element exists
            scroller.style.animationPlayState = 'running';
        }
    });
}

// Success popup timeout - This can likely stay global if the popup ID is unique
setTimeout(() => {
  const popup = document.getElementById('successPopup');
  if (popup) popup.remove();
}, 5000);