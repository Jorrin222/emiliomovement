(function () {
    var STORAGE_KEY = 'em_consent';

    function updateConsent(value) {
        if (typeof gtag === 'function') {
            gtag('consent', 'update', {
                ad_storage: value,
                analytics_storage: value,
                ad_user_data: value,
                ad_personalization: value
            });
        }
    }

    function hideBanner() {
        var banner = document.getElementById('cookie-banner');
        if (banner) {
            banner.classList.add('cookie-banner--hidden');
        }
    }

    function init() {
        var stored = localStorage.getItem(STORAGE_KEY);
        if (stored) return; // already decided

        var banner = document.getElementById('cookie-banner');
        if (!banner) return;

        banner.classList.add('cookie-banner--visible');

        document.getElementById('cookie-accept').addEventListener('click', function () {
            localStorage.setItem(STORAGE_KEY, 'granted');
            updateConsent('granted');
            hideBanner();
        });

        document.getElementById('cookie-decline').addEventListener('click', function () {
            localStorage.setItem(STORAGE_KEY, 'denied');
            hideBanner();
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
