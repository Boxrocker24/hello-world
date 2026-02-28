(() => {
    function setupMobileNav() {
        const button = document.getElementById("mobile-nav-button");
        const menu = document.getElementById("mobile-nav");

        if (!button || !menu) {
            return;
        }

        const setOpen = (open) => {
            menu.classList.toggle("hidden", !open);
            button.setAttribute("aria-expanded", open ? "true" : "false");
        };

        button.addEventListener("click", () => {
            const isOpen = button.getAttribute("aria-expanded") === "true";
            setOpen(!isOpen);
        });

        menu.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => setOpen(false));
        });

        window.addEventListener("resize", () => {
            if (window.innerWidth >= 768) {
                setOpen(false);
            }
        });
    }

    function setupContactForm() {
        const form = document.getElementById("contact-form");
        const success = document.getElementById("contact-success");

        if (!form || !success) {
            return;
        }

        form.addEventListener("submit", (event) => {
            event.preventDefault();

            if (!form.checkValidity()) {
                form.reportValidity();
                return;
            }

            form.reset();
            success.classList.remove("hidden");
            success.focus();
        });
    }

    document.addEventListener("DOMContentLoaded", () => {
        setupMobileNav();
        setupContactForm();
    });
})();
