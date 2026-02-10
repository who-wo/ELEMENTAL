/* ============================================
   Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

    // --- Header scroll effect ---
    const header = document.getElementById('siteHeader');
    if (header) {
        window.addEventListener('scroll', () => {
            header.classList.toggle('scrolled', window.scrollY > 50);
        });
    }

    // --- Mobile hamburger menu ---
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('headerNav');

    if (hamburger && nav) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            nav.classList.toggle('open');
        });

        // Close menu on link click
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                nav.classList.remove('open');
            });
        });

        // Close menu on outside click
        document.addEventListener('click', (e) => {
            if (!nav.contains(e.target) && !hamburger.contains(e.target)) {
                hamburger.classList.remove('active');
                nav.classList.remove('open');
            }
        });
    }

    // --- Search overlay ---
    const searchToggle = document.getElementById('searchToggle');
    const searchOverlay = document.getElementById('searchOverlay');
    const searchClose = document.getElementById('searchClose');

    if (searchToggle && searchOverlay) {
        searchToggle.addEventListener('click', () => {
            searchOverlay.classList.add('active');
            const input = searchOverlay.querySelector('input');
            if (input) setTimeout(() => input.focus(), 200);
        });

        if (searchClose) {
            searchClose.addEventListener('click', () => {
                searchOverlay.classList.remove('active');
            });
        }

        // Close on ESC
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                searchOverlay.classList.remove('active');
            }
        });

        // Close on overlay click
        searchOverlay.addEventListener('click', (e) => {
            if (e.target === searchOverlay) {
                searchOverlay.classList.remove('active');
            }
        });
    }

    // --- Scroll animations (fade-in) ---
    const fadeElements = document.querySelectorAll('.fade-in');

    if (fadeElements.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        fadeElements.forEach(el => observer.observe(el));
    }

    // --- Auto-hide flash messages ---
    const flashMsgs = document.querySelectorAll('.flash-msg');
    flashMsgs.forEach((msg, i) => {
        setTimeout(() => {
            msg.style.opacity = '0';
            msg.style.transform = 'translateX(100%)';
            setTimeout(() => msg.remove(), 400);
        }, 3000 + (i * 500));
    });

    // --- Smooth scroll for anchor links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});
