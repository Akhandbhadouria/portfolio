/* ============================================
   Portfolio JavaScript — Akhand Pratapsingh
   Scroll animations, navigation, cursor glow
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ---- Cursor Glow ----
  const cursorGlow = document.getElementById('cursorGlow');
  if (cursorGlow) {
    let mouseX = 0, mouseY = 0;
    let glowX = 0, glowY = 0;

    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    function animateCursor() {
      glowX += (mouseX - glowX) * 0.08;
      glowY += (mouseY - glowY) * 0.08;
      cursorGlow.style.left = glowX + 'px';
      cursorGlow.style.top = glowY + 'px';
      requestAnimationFrame(animateCursor);
    }
    animateCursor();
  }

  // ---- Scroll Reveal ----
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -60px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // ---- Skill Bar Animation ----
  const skillBars = document.querySelectorAll('.skill-bar-fill');

  const barObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target;
        const width = bar.getAttribute('data-width');
        bar.style.width = width + '%';
        bar.classList.add('animate');
        barObserver.unobserve(bar);
      }
    });
  }, {
    threshold: 0.3
  });

  skillBars.forEach(bar => barObserver.observe(bar));

  // ---- Active Navigation ----
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-pill a');

  function updateActiveNav() {
    const scrollY = window.scrollY + window.innerHeight / 2;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionBottom = sectionTop + section.offsetHeight;
      const sectionId = section.getAttribute('id');

      if (scrollY >= sectionTop && scrollY < sectionBottom) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + sectionId) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', updateActiveNav, { passive: true });
  updateActiveNav();

  // ---- Smooth scroll for nav links ----
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href');
      const targetSection = document.querySelector(targetId);
      if (targetSection) {
        targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ---- Parallax on Hero Image ----
  const heroImage = document.querySelector('.hero-image-wrapper img');
  if (heroImage) {
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      if (scrollY < window.innerHeight) {
        heroImage.style.transform = `translateY(${scrollY * 0.15}px) scale(1.05)`;
      }
    }, { passive: true });
  }

  // ---- 3D Project Carousel ----
  const track = document.getElementById('carouselTrack');
  const cards = document.querySelectorAll('.carousel-card');
  const dots = document.querySelectorAll('.carousel-dot');
  const viewport = document.getElementById('carouselViewport');

  if (track && cards.length > 0) {
    let currentIndex = 0;
    const totalCards = cards.length;
    let autoplayTimer = null;

    // Calculate card width + gap for positioning
    function getCardStep() {
      const card = cards[0];
      const style = getComputedStyle(track);
      const gap = parseInt(style.gap) || 28;
      return card.offsetWidth + gap;
    }

    // Update 3D positions & track translate
    function updateCarousel(animate = true) {
      const step = getCardStep();
      const offset = -currentIndex * step;

      if (animate) {
        track.style.transition = 'transform 0.55s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
      } else {
        track.style.transition = 'none';
      }
      track.style.transform = `translateX(${offset}px)`;

      // Set data-position for 3D CSS
      cards.forEach((card, i) => {
        const pos = i - currentIndex;
        const clampedPos = Math.max(-3, Math.min(3, pos));
        card.setAttribute('data-position', clampedPos);
      });

      // Update dots
      dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === currentIndex);
      });
    }

    // Navigate to specific index
    function goTo(index) {
      currentIndex = Math.max(0, Math.min(totalCards - 1, index));
      updateCarousel();
    }

    // Auto-scroll left → right → left
    let autoDirection = 1;
    function startAutoplay() {
      stopAutoplay();
      autoplayTimer = setInterval(() => {
        if (currentIndex >= totalCards - 1) autoDirection = -1;
        if (currentIndex <= 0) autoDirection = 1;
        goTo(currentIndex + autoDirection);
      }, 3000);
    }

    function stopAutoplay() {
      if (autoplayTimer) clearInterval(autoplayTimer);
    }

    // Dot click
    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const idx = parseInt(dot.getAttribute('data-index'));
        goTo(idx);
        stopAutoplay();
        startAutoplay();
      });
    });

    // Drag / swipe support
    let isDragging = false;
    let dragStartX = 0;
    let dragDelta = 0;

    viewport.addEventListener('mousedown', (e) => {
      isDragging = true;
      dragStartX = e.clientX;
      dragDelta = 0;
      stopAutoplay();
      track.style.transition = 'none';
    });

    viewport.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      dragDelta = e.clientX - dragStartX;
      const step = getCardStep();
      const offset = -currentIndex * step + dragDelta;
      track.style.transform = `translateX(${offset}px)`;
    });

    viewport.addEventListener('mouseup', () => {
      if (!isDragging) return;
      isDragging = false;
      const step = getCardStep();
      if (Math.abs(dragDelta) > step * 0.2) {
        if (dragDelta < 0) goTo(currentIndex + 1);
        else goTo(currentIndex - 1);
      } else {
        updateCarousel();
      }
      startAutoplay();
    });

    viewport.addEventListener('mouseleave', () => {
      if (isDragging) {
        isDragging = false;
        updateCarousel();
        startAutoplay();
      }
    });

    // Touch support
    viewport.addEventListener('touchstart', (e) => {
      isDragging = true;
      dragStartX = e.touches[0].clientX;
      dragDelta = 0;
      stopAutoplay();
      track.style.transition = 'none';
    }, { passive: true });

    viewport.addEventListener('touchmove', (e) => {
      if (!isDragging) return;
      dragDelta = e.touches[0].clientX - dragStartX;
      const step = getCardStep();
      const offset = -currentIndex * step + dragDelta;
      track.style.transform = `translateX(${offset}px)`;
    }, { passive: true });

    viewport.addEventListener('touchend', () => {
      if (!isDragging) return;
      isDragging = false;
      const step = getCardStep();
      if (Math.abs(dragDelta) > step * 0.2) {
        if (dragDelta < 0) goTo(currentIndex + 1);
        else goTo(currentIndex - 1);
      } else {
        updateCarousel();
      }
      startAutoplay();
    });

    // Scroll-based carousel navigation
    const carouselObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          startAutoplay();
        } else {
          stopAutoplay();
        }
      });
    }, { threshold: 0.3 });

    carouselObserver.observe(viewport);

    // Keyboard arrows when carousel is in view
    document.addEventListener('keydown', (e) => {
      const rect = viewport.getBoundingClientRect();
      const isVisible = rect.top < window.innerHeight && rect.bottom > 0;
      if (!isVisible) return;

      if (e.key === 'ArrowRight') { goTo(currentIndex + 1); stopAutoplay(); startAutoplay(); }
      if (e.key === 'ArrowLeft') { goTo(currentIndex - 1); stopAutoplay(); startAutoplay(); }
    });

    // Initial render
    updateCarousel(false);
  }

  // ---- Typing Effect for Hero Name (subtle) ----
  const heroName = document.querySelector('.hero-name');
  if (heroName) {
    heroName.style.opacity = '0';
    heroName.style.transform = 'translateY(30px)';

    setTimeout(() => {
      heroName.style.transition = 'opacity 1s ease, transform 1s ease';
      heroName.style.opacity = '1';
      heroName.style.transform = 'translateY(0)';
    }, 300);
  }

  // ---- Staggered Hero Contact Items ----
  const contactItems = document.querySelectorAll('.hero-contact-item');
  contactItems.forEach((item, index) => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(20px)';

    setTimeout(() => {
      item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      item.style.opacity = '1';
      item.style.transform = 'translateY(0)';
    }, 800 + index * 150);
  });

  // ---- Hero Badge Animation ----
  const heroBadge = document.querySelector('.hero-badge');
  if (heroBadge) {
    heroBadge.style.opacity = '0';
    heroBadge.style.transform = 'translateY(15px)';

    setTimeout(() => {
      heroBadge.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      heroBadge.style.opacity = '1';
      heroBadge.style.transform = 'translateY(0)';
    }, 200);
  }

  // ---- Counter Animation for Stats (if added) ----
  function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const startTime = performance.now();

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(eased * target);

      element.textContent = current;

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        element.textContent = target;
      }
    }

    requestAnimationFrame(update);
  }

  // ---- Nav hide/show on scroll ----
  let lastScrollY = window.scrollY;
  const navWrapper = document.getElementById('mainNav');

  window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;

    if (currentScrollY > lastScrollY && currentScrollY > 400) {
      navWrapper.style.transform = 'translateX(-50%) translateY(120px)';
      navWrapper.style.opacity = '0';
    } else {
      navWrapper.style.transform = 'translateX(-50%) translateY(0)';
      navWrapper.style.opacity = '1';
    }

    navWrapper.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
    lastScrollY = currentScrollY;
  }, { passive: true });

});
