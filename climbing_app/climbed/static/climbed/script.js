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

    // Calendar functions
    const dayDivsEvent = () => {
        const dayDivs = document.querySelectorAll(".day-element");
        dayDivs.forEach(dayDiv => {
            dayDiv.addEventListener("click", showForm);
        });
    }

    const buttons = document.querySelectorAll(".calendar header a");
    buttons.forEach(button => {
        button.addEventListener("click", (event) => {
            event.preventDefault();
            
            const url = button.getAttribute("href");
            fetch(url)
            .then(response => response.json())
            .then(date => {
                updateCalendar(date);
                dayDivsEvent();
            });
        });
    });

    dayDivsEvent();
    
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

    // Changing calendar grid
    calendarGrid.innerHTML = "";
    for (const day of date.days_list) {
        const dayDiv = document.createElement("div")
        dayDiv.classList.add("day-element");

        const p = document.createElement("p");
        if (day === date.current_day && date.is_now_month && date.is_now_year) {
            p.classList.add("selected-day");
        }
        p.innerText = day;
        
        const taskDiv = document.createElement("div")
        taskDiv.classList.add("task");

        dayDiv.appendChild(p);
        dayDiv.appendChild(taskDiv);

        calendarGrid.appendChild(dayDiv);
    }
}

function showForm() {
    const calendar = document.querySelector(".calendar");
    const formHTML = `
        <header style="flex-direction: column;"><h1>Add workout</h1></header>
        <form action="{% url 'add_workout' %}" method="POST" class="form-workout">
            <div class="column">
                <div class="form-group">
                    <label for="workout_title">Workout title</label>
                    <input type="text" name="workout_title" id="workout_title" placeholder="Add workout title" required>
                </div>
                <div class="form-group">
                    <label for="workout_type">Workout type</label>
                    <input type="text" name="workout_type" id="workout_type" placeholder="power/endurance/finger power etc." required>
                </div>
                <div class="form-group">
                    <label for="planned_tiredness">Planned tiredness</label>
                    <select name="planned_tiredness" id="planned_tiredness" required>
                        <option value="" disabled selected>Select planned tiredness level</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </div>
            </div>
            <div class="column">
                <div class="form-group">
                    <label for="date">Workout date</label>
                    <input type="date" name="date cols="3" required>
                </div>
                <div class="form-group">
                    <label for="workout_description">Workout description</label>
                    <textarea name="workout_description cols="3"
                     id="workout_description" placeholder="What you will be doing on the training" required></textarea>
                </div>
            </div>
            <span></span>
            <input style="height: 50px; margin-right: auto;"; class="submit-button" type="submit" value="Save">
        </form>  
    `
    
    calendar.innerHTML = formHTML; 
}
