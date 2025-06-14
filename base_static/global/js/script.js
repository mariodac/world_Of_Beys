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

function previewImage(event) {
    const input = event.target;
    const preview = document.getElementById("preview");

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = "block";
        };

        reader.readAsDataURL(input.files[0]);
    }
}

document.addEventListener("click", function (event) {
    const dropdown = document.getElementById("dropdown");
    const selector = document.querySelector(".custom-select-selected");

    if (!selector.contains(event.target)) {
        dropdown.style.display = "none";
    }
});

function toggleDropdownType(event) {
    event.stopPropagation();
    const dropdown = document.getElementById("dropdown");
    dropdown.style.display =
        dropdown.style.display === "block" ? "none" : "block";
}

function selectOption(option) {
    const selectedText = option.textContent.trim();
    const value = option.getAttribute("data-value");
    const img = option.querySelector("img").src;
    document.getElementById("selected-text").textContent = selectedText;
    const icon = document.querySelector(".custom-select-selected img");
    if (icon) icon.src = img;
    else {
        const span = document.getElementById("selected-text");
        span.insertAdjacentHTML(
            "beforebegin",
            `<img src="${img}" class="icon-logo"> `
        );
    }
    document.getElementById("type_bey").value = value;
    document.getElementById("dropdown").style.display = "none";
    document.getElementById("selected-type-icon").style.display = "none";
}

document.addEventListener("click", function (event) {
    const dropdown = document.getElementById("dropdown-system");
    const selector = document.querySelector(".custom-select-selected");

    if (!selector.contains(event.target)) {
        dropdown.style.display = "none";
    }
});

function toggleDropdownSystem(event) {
    event.stopPropagation();
    const dropdown = document.getElementById("dropdown-system");
    dropdown.style.display =
        dropdown.style.display === "block" ? "none" : "block";
}

function selectSystem(option) {
    const selectedText = option.textContent.trim();
    const value = option.getAttribute("data-value");
    const img = option.querySelector("img").src;
    document.getElementById("selected-system-text").textContent = selectedText;
    const icon = document.querySelector(
        ".custom-select-selected img#system-icon"
    );
    // const icon = document.getElementById("selected-system-icon");
    if (icon) icon.src = img;
    else {
        const span = document.getElementById("selected-system-text");
        span.insertAdjacentHTML(
            "beforebegin",
            `<img id="system-icon" src="${img}" class="icon-logo"> `
        );
    }
    document.getElementById("system_bey").value = value;
    document.getElementById("dropdown-system").style.display = "none";
    document.getElementById("selected-system-icon").style.display = "none";
}
