function toggleTheme() {
    const root = document.documentElement;
    const currentTheme = root.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    const toggleBtn = document.getElementById("themeToggle");
    root.setAttribute("data-theme", newTheme);
    const icon = newTheme === "dark" ? "☀️" : "🌙";
    const text = newTheme === "dark" ? "Modo claro" : "Modo escuro";
    toggleBtn.innerText = `${icon} ${text}`;
    toggleBtn.setAttribute("data-icon", icon);
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
