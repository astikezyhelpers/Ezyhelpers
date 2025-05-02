document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const blogPosts = document.querySelectorAll('.blog-post'); // Ensure each blog post has this class
  
    // Function to filter blog posts
    function filterPosts() {
        const searchTerm = searchInput.value.trim().toLowerCase();
        let hasResults = false;
        
        blogPosts.forEach(post => {
          const title = post.querySelector('.blog-title').textContent.toLowerCase();
          const content = post.querySelector('.blog-content')?.textContent.toLowerCase() || '';
          
          if (title.includes(searchTerm)) {
            post.style.display = 'block';
            hasResults = true;
          } else if (content.includes(searchTerm)) {
            post.style.display = 'block';
            hasResults = true;
          } else {
            post.style.display = 'none';
          }
        });
      
        // Show "No results" message if needed
        const noResultsMsg = document.getElementById('noResultsMsg');
        if (!hasResults && searchTerm) {
          if (!noResultsMsg) {
            const msg = document.createElement('p');
            msg.id = 'noResultsMsg';
            msg.textContent = 'No posts found. Try a different search term.';
            document.querySelector('.blog-container').appendChild(msg);
          }
        } else if (noResultsMsg) {
          noResultsMsg.remove();
        }
      }
  
    // Event listener for the search button
    searchButton.addEventListener('click', filterPosts);
  
    // Event listener for the search input (for real-time filtering)
    searchInput.addEventListener('input', filterPosts);
  });