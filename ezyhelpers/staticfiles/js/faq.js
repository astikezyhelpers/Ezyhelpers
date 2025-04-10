document.querySelectorAll('.py-6 button').forEach(button => {
    button.addEventListener('click', () => {
      const faqItem = button.closest('.py-6');
      const answer = faqItem.querySelector('.faq-answer');
      const icon = button.querySelector('.fa-plus');
      
      // Close all other FAQ items first
      document.querySelectorAll('.py-6').forEach(item => {
        if (item !== faqItem) {
          item.querySelector('.faq-answer').classList.remove('show');
          item.querySelector('.fa-plus').classList.remove('rotate-45');
        }
      });
      
      // Toggle the clicked FAQ item
      answer.classList.toggle('show');
      icon.classList.toggle('rotate-45');
    });
  });