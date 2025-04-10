    // Video Modal functionality
    const videoModal = document.getElementById('videoModal');
    const closeModal = document.getElementById('closeModal');
    const videoFrame = document.getElementById('videoFrame');
    const watchVideoBtns = document.querySelectorAll('a:has(i.fa-play-circle)'); // Selects all "Watch Video" buttons
  
    watchVideoBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        // Replace this with your actual YouTube video ID
        videoFrame.src = "https://www.youtube.com/embed/557O9bibao8?si=AioQ8mnWH2PZkOED";
        videoModal.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });
  
    closeModal.addEventListener('click', () => {
      videoModal.classList.remove('active');
      videoFrame.src = "";
      document.body.style.overflow = 'auto';
    });
  
    // Close modal when clicking outside video
    videoModal.addEventListener('click', (e) => {
      if (e.target === videoModal) {
        videoModal.classList.remove('active');
        videoFrame.src = "";
        document.body.style.overflow = 'auto';
      }
    });