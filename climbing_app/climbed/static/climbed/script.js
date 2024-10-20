document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll(".image-with-loader");

    images.forEach(image => {
        // Function to hide the loader and show the image
        const hideLoader = () => {
            const loader = image.previousElementSibling; // The loader div
            if (loader) {
                loader.style.display = "none"; // Hide loader
            }
            image.style.opacity = 1; // Fade in the image
        };

        // Check if the image is already loaded from cache
        if (image.complete) {
            hideLoader(); // If cached, hide the loader immediately
        } else {
            // Event listener to hide loader and show image once it's fully loaded
            image.addEventListener("load", hideLoader);

            // Fallback in case the image fails to load
            image.addEventListener("error", function() {
                const loader = image.previousElementSibling;
                if (loader) {
                    loader.style.display = "none"; // Hide loader on error
                }
                image.alt = "Image failed to load"; // Provide alternate text
            });
        }
    });

    const buttons = document.querySelectorAll(".calendar header a");
    buttons.forEach(button => {
        button.addEventListener("click", (event) => {
            event.preventDefault();
            
            const url = button.getAttribute("href");
            fetch(url)
            .then(response => response.json())
            .then(date => {
                updateCalendar(date);
            });
        });
    });
});

function updateCalendar(date) { 
    const calendar = document.querySelector(".calendar");
    const monthH1 = document.getElementById("month-h1");
    const yearH1 = document.getElementById("year-h1");
    const calendarGrid = calendar.querySelector(".calendar-grid");
    const buttons = document.querySelectorAll(".calendar header a");

    // Change month h1
    monthH1.innerText = date.current_month_string;
    yearH1.innerText = date.current_year;

    // Change buttons inner values
    buttons[0].href = `get_month/previous/${date.current_month_number}/${date.current_year}`;
    buttons[1].href = `get_month/next/${date.current_month_number}/${date.current_year}`;
}
