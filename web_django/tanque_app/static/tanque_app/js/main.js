document.addEventListener("DOMContentLoaded", function() {
    
    // --- LÓGICA DEL MODO OSCURO ---
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');
    const htmlElement = document.documentElement;
    
    // Función para cambiar el icono
    const updateIcon = (theme) => {
        if(theme === 'dark') {
            themeIcon.classList.replace('bi-moon-stars-fill', 'bi-sun-fill');
        } else {
            themeIcon.classList.replace('bi-sun-fill', 'bi-moon-stars-fill');
        }
    };

    // Comprobar si hay un tema guardado en LocalStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-bs-theme', savedTheme);
        updateIcon(savedTheme);
    }

    // Evento click para alternar temas
    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        htmlElement.setAttribute('data-bs-theme', newTheme);
        updateIcon(newTheme);
        
        // Guardar preferencia en LocalStorage
        localStorage.setItem('theme', newTheme);
    });
    // ------------------------------

    // Preparar campos de Django para que funcionen con Floating Labels
    const inputs = document.querySelectorAll('#sim-form input');
    inputs.forEach(input => {
        if(input.type !== 'hidden' && input.type !== 'submit') {
            input.classList.add('form-control');
            if(!input.getAttribute('placeholder')) {
                input.setAttribute('placeholder', 'Valor');
            }
        }
    });

    // Manejo del botón de submit (Loading state)
    const form = document.getElementById("sim-form");
    const btnSubmit = document.getElementById("btn-submit");
    const btnText = document.getElementById("btn-text");
    const btnSpinner = document.getElementById("btn-spinner");

    if(form) {
        form.addEventListener("submit", function() {
            btnSubmit.disabled = true;
            btnSubmit.style.opacity = "0.9";
            btnText.innerHTML = "Calculando...";
            btnSpinner.classList.remove("d-none");
        });
    }
});
