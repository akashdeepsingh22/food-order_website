// Check if user is logged in
function isLoggedIn() {
    return localStorage.getItem("loggedIn") === "true";
}
// Handle login
function loginUser() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Basic validation (replace with actual server-side authentication)
    if (username === "user" && password === "password") {
        localStorage.setItem("loggedIn", "true");
        alert("Login successful!");
        window.location.href = "index.html"; // Redirect to homepage after login
    } else {
        alert("Invalid credentials! Try again.");
    }
}

// Slideshow functionality
let currentSlide = 0;
const slides = document.querySelectorAll(".slide");

function showSlide() {
    slides.forEach((slide, index) => {
        slide.style.display = "none";
    });
    currentSlide++;
    if (currentSlide > slides.length) { currentSlide = 1 }
    slides[currentSlide - 1].style.display = "block";
}

setInterval(showSlide, 3000); // Change image every 3 seconds
showSlide(); // Initial display






