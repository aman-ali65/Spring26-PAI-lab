// ========================================
// WEATHER APP - THEME MANAGEMENT
// ========================================

console.log('Weather App JavaScript Loaded!');

function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    updateThemeIcon(newTheme);
    console.log('Theme switched to:', newTheme);
}

function updateThemeIcon(theme) {
    const icon = document.querySelector('.theme-icon');
    if (icon) {
        icon.textContent = theme === 'light' ? '☀️' : '🌙';
    }
}

function loadSavedTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
    console.log('Loaded theme:', savedTheme);
}

// Load theme on page load
window.addEventListener('DOMContentLoaded', loadSavedTheme);

// Form handling functions
function switchTab(tabName) {
    console.log('Switching to tab:', tabName);
    
    // Get all buttons and forms
    const buttons = document.querySelectorAll('.tab-button');
    const forms = document.querySelectorAll('.search-form');
    
    // Remove active class from all buttons and forms
    buttons.forEach(btn => btn.classList.remove('active'));
    forms.forEach(form => {
        form.classList.remove('active');
        form.style.display = 'none';
    });
    
    // Add active class to clicked button
    event.target.classList.add('active');
    
    // Show the corresponding form
    const targetForm = document.getElementById(tabName + '-form');
    if (targetForm) {
        targetForm.classList.add('active');
        targetForm.style.display = 'block';
        console.log('Form displayed:', tabName + '-form');
    } else {
        console.error('Form not found:', tabName + '-form');
    }
}

function submitInfo() {
    console.log('submitInfo called');
    const city = document.getElementById('info-city').value.trim();
    console.log('City value:', city);
    if (city) {
        window.location.href = `/info/${encodeURIComponent(city)}`;
    } else {
        alert('Please enter a city name');
    }
}

function submitCurrent() {
    console.log('submitCurrent called');
    const city = document.getElementById('current-city').value.trim();
    console.log('City value:', city);
    if (city) {
        window.location.href = `/current/${encodeURIComponent(city)}`;
    } else {
        alert('Please enter a city name');
    }
}

function submitCoords() {
    console.log('submitCoords called');
    const lng = document.getElementById('longitude').value;
    const lat = document.getElementById('latitude').value;
    console.log('Coordinates:', lng, lat);
    if (lng && lat) {
        window.location.href = `/weather?lng=${lng}&lat=${lat}`;
    } else {
        alert('Please enter both longitude and latitude');
    }
}

function submitHistory() {
    console.log('submitHistory called');
    const city = document.getElementById('history-city').value.trim();
    const from = document.getElementById('from-date').value;
    const to = document.getElementById('to-date').value;
    console.log('History params:', city, from, to);
    
    if (city && from && to) {
        const fromFormatted = from.replace('T', ' ') + ':00';
        const toFormatted = to.replace('T', ' ') + ':00';
        window.location.href = `/history/${encodeURIComponent(city)}?from=${encodeURIComponent(fromFormatted)}&to=${encodeURIComponent(toFormatted)}`;
    } else {
        alert('Please fill in all fields: city, from date, and to date');
    }
}

// Allow Enter key to submit forms
document.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        const activeForm = document.querySelector('.search-form.active');
        if (activeForm) {
            const button = activeForm.querySelector('.submit-button');
            if (button) {
                console.log('Enter key pressed, clicking button');
                button.click();
            }
        }
    }
});
