function toggleTheme() {
    const root = document.documentElement;
    const currentTheme = root.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    const toggleBtn = document.getElementById("themeToggle");
    root.setAttribute("data-theme", newTheme);
    const icon = newTheme === "dark" ? "☀️" : "🌙";
    const text = newTheme === "dark" ? "Light mode" : "Dark mode";
    toggleBtn.innerText = `${icon} ${text}`;
    toggleBtn.setAttribute("data-icon", icon);
    localStorage.setItem("theme", newTheme);
}
function toggleMenu() {
    const menu = document.getElementById("menu");
    const button = document.getElementById("menuToggle");
    menu.classList.toggle("visible");
    button.classList.toggle("open");
}

let dropdownTimeout;

function toggleDropdown(event) {
    const dropdown = event.currentTarget.parentElement;
    dropdown.classList.toggle("open");
    clearTimeout(dropdownTimeout);
    if (dropdown.classList.contains("open")) {
        dropdownTimeout = setTimeout(() => {
            dropdown.classList.remove("open");
        }, 2000);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);
    document.querySelectorAll(".dropdown").forEach((dropdown) => {
        dropdown.addEventListener("mouseenter", () => {
            dropdown.classList.add("open");
            clearTimeout(dropdownTimeout);
        });
        dropdown.addEventListener("mouseleave", () => {
            dropdownTimeout = setTimeout(() => {
                dropdown.classList.remove("open");
            }, 300);
        });
    });
});

function toggleVisibility(btn) {
    const part = btn.closest(".part");
    part.classList.toggle("hidden");
}

function applyFilters() {
    const search = document.getElementById("searchInput").value.toLowerCase();
    const type = document.getElementById("filterType").value;
    const parts = document.querySelectorAll(".part");

    parts.forEach((part) => {
        const name = part.dataset.name.toLowerCase();
        const ptype = part.dataset.type;
        const matchSearch = name.includes(search);
        const matchType = type === "" || type === ptype;
        part.style.display = matchSearch && matchType ? "block" : "none";
    });
}

function sortParts() {
    const container = document.getElementById("partsList");
    const parts = Array.from(container.querySelectorAll(".part"));

    parts.sort((a, b) => {
        return a.dataset.name.localeCompare(b.dataset.name);
    });

    parts.forEach((p) => container.appendChild(p));
}
