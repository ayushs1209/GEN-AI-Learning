document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Set initial button text based on default mode (which is 'dark-mode' from HTML)
    // The class is added in HTML, so we check for the *absence* of light-mode
    if (body.classList.contains('dark-mode')) {
         themeToggle.textContent = 'Light Mode'; // In dark mode, button text is "Light Mode"
    } else {
         themeToggle.textContent = 'Dark Mode'; // In light mode, button text is "Dark Mode"
    }


    themeToggle.addEventListener('click', () => {
        // Check the current mode
        if (body.classList.contains('dark-mode')) {
            // If currently dark, switch to light
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
            themeToggle.textContent = 'Dark Mode'; // Button now says "Dark Mode" (to switch back)
        } else {
            // If currently light (or neither, though we start dark), switch to dark
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
            themeToggle.textContent = 'Light Mode'; // Button now says "Light Mode" (to switch back)
        }

        // Optional: Save preference in localStorage (persists across sessions)
        const currentMode = body.classList.contains('dark-mode') ? 'dark' : 'light';
        localStorage.setItem('theme', currentMode);
    });

    // Optional: Apply saved preference on page load
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.classList.remove('dark-mode', 'light-mode'); // Remove any existing classes
        body.classList.add(`${savedTheme}-mode`); // Add the saved mode class

         if (savedTheme === 'dark') {
             themeToggle.textContent = 'Light Mode';
         } else {
             themeToggle.textContent = 'Dark Mode';
         }
    }
     // If no saved theme, it defaults to the class set in HTML ('dark-mode')

});