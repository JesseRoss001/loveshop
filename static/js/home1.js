document.addEventListener('DOMContentLoaded', function () {
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
      // Reduce the number of hearts and introduce a delay
      for (let i = 0; i < 2; i++) {
        let heart = document.createElement('i');
        let delay = Math.random() * 5; // Delay up to 5 seconds
        heart.classList.add('fas', 'fa-heart', 'falling-heart');
        heart.style.left = `${Math.floor(Math.random() * 100)}vw`;
        heart.style.animationDuration = `${Math.random() * 3 + 15}s`; // Increase duration for a slower fall
        heart.style.animationDelay = `${delay}s`; // Apply random delay
        heart.style.opacity = `${Math.random() * 0.5 + 0.5}`;
        document.body.appendChild(heart);

        // Remove heart after it falls to keep the DOM clean
        heart.addEventListener('animationend', function() {
          heart.remove();
        });
      }
    }
  });