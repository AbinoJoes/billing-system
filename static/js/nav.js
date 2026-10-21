document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("sidebarToggle");
    const sidebar = document.getElementById("sidebar");
    const sidebarClose = document.getElementById("sidebarClose");
    const backdrop = document.getElementById("sidebarBackdrop");

    console.log("Toggle:", menuToggle);
    console.log("Sidebar:", sidebar);

    if (!menuToggle || !sidebar) {
        console.error("Sidebar button or sidebar not found.");
        return;
    }

    function toggleSidebar() {
        const isOpen = sidebar.classList.toggle("active");

        if (backdrop) {
            backdrop.classList.toggle("active", isOpen);
        }

        menuToggle.setAttribute("aria-expanded", String(isOpen));
    }

    function closeSidebar() {
        sidebar.classList.remove("active");

        if (backdrop) {
            backdrop.classList.remove("active");
        }

        menuToggle.setAttribute("aria-expanded", "false");
    }

    menuToggle.addEventListener("click", toggleSidebar);

    if (sidebarClose) {
        sidebarClose.addEventListener("click", closeSidebar);
    }

    if (backdrop) {
        backdrop.addEventListener("click", closeSidebar);
    }
});


