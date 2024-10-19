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
});
