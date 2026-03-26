/* 
 * Emilio Movement - V10 Scripts (Tactile Minimalism)
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Lucide Icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // 2. Mobile Navigation Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    const body = document.body;

    if (mobileMenuBtn && navLinks) {
        function toggleMenu() {
            const isOpen = navLinks.classList.contains('open');

            navLinks.classList.toggle('open');
            body.classList.toggle('body-no-scroll');

            // Toggle Menu/X icon
            if (!isOpen) {
                mobileMenuBtn.innerHTML = '<i data-lucide="x"></i>';
            } else {
                mobileMenuBtn.innerHTML = '<i data-lucide="menu"></i>';
            }

            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        }

        mobileMenuBtn.addEventListener('click', toggleMenu);

        // Close menu when clicking a link
        const navItems = navLinks.querySelectorAll('.nav-link');
        navItems.forEach(item => {
            item.addEventListener('click', () => {
                if (navLinks.classList.contains('open')) {
                    toggleMenu();
                }
            });
        });
    }

    // 3. Header Scroll Effect - very subtle for V10
    const header = document.querySelector('.site-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });

        // Trigger initial check
        if (window.scrollY > 20) {
            header.classList.add('scrolled');
        }
    }

    // 4. Slow, Deliberate Reveal Animation & Line Drawing
    // V10 uses a very grounded, slow slide-up
    const revealElements = document.querySelectorAll('.reveal, .line-draw, .reveal-text, .slide-up, .slide-up-delay, .slide-up-delay-2, .slide-up-delay-3, .block-reveal');

    if (revealElements.length > 0) {
        const revealOptions = {
            root: null,
            rootMargin: '0px 0px -50px 0px',
            threshold: 0.15
        };

        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, revealOptions);

        revealElements.forEach(element => {
            revealObserver.observe(element);
        });

        // Forcefully reveal elements already in viewport on load for immediate tactile feel
        setTimeout(() => {
            revealElements.forEach(element => {
                const rect = element.getBoundingClientRect();
                if (rect.top < window.innerHeight) {
                    element.classList.add('active');
                }
            });
        }, 50);
    }

    // 5. Active Link Highlighting
    const currentPath = window.location.pathname;
    const navItemsList = document.querySelectorAll('.nav-link');

    navItemsList.forEach(item => {
        const href = item.getAttribute('href');

        if (
            currentPath.includes(href) ||
            (currentPath.endsWith('/') && href === 'index.html') ||
            (currentPath.endsWith('/v10/') && href === 'index.html') ||
            (currentPath.endsWith('/v11/') && href === 'index.html')
        ) {
            item.classList.add('active');
        }
    });

    // 6. Service Card Video Hover Play/Pause
    document.querySelectorAll('.service-card').forEach(card => {
        const video = card.querySelector('video.hover-media');
        if (video) {
            card.addEventListener('mouseenter', () => video.play());
            card.addEventListener('mouseleave', () => { video.pause(); video.currentTime = 0; });
        }
    });

    // 7. Footer year
    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    // 8. FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');
    if (faqItems.length > 0) {
        faqItems.forEach(item => {
            const questionBtn = item.querySelector('.faq-question');

            questionBtn.addEventListener('click', () => {
                const isActive = item.classList.contains('active');

                // Close all items
                faqItems.forEach(faqItem => {
                    faqItem.classList.remove('active');
                    const answer = faqItem.querySelector('.faq-answer');
                    if (answer) answer.style.maxHeight = null;
                });

                // If it wasn't active, open it
                if (!isActive) {
                    item.classList.add('active');
                    const answer = item.querySelector('.faq-answer');
                    if (answer) answer.style.maxHeight = answer.scrollHeight + "px";
                }
            });
        });
    }
});
