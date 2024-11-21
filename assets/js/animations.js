// Save as assets/js/animations.js
document.addEventListener('DOMContentLoaded', function() {
    // Intersection Observer for fade-in animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, {
      threshold: 0.1
    });
  
    // Observe all sections
    document.querySelectorAll('section').forEach((section) => {
      observer.observe(section);
    });
  
    // Animate stat numbers
    const animateValue = (obj, start, end, duration) => {
      let startTimestamp = null;
      const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = Math.floor(progress * (end - start) + start);
        if (progress < 1) {
          window.requestAnimationFrame(step);
        }
      };
      window.requestAnimationFrame(step);
    };
  
    // Animate stats when they come into view
    document.querySelectorAll('.stat-card h3').forEach((stat) => {
      observer.observe(stat);
    });
  });