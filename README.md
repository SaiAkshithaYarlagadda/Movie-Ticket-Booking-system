 Movie-Ticket-Booking-system

This is a simple full-stack Movie Ticket Booking System built using Python Flask(backend) and HTML/CSS/JavaScript (frontend). It allows users to:

1. Book movie tickets
2.Order food (Popcorn, Coke, Nachos)
3.Simulate a payment process
4.Get a Booking ID and confirmation
5. All in a beautiful single-page interface

Features

1.Movie listing with available seats
2. Ticket booking with user details
3.Food menu with item-wise cost
4.Payment simulation with card & CVV validation
5.Flash messages for booking success or failure
6.Secure backend logic using Flask

Technologies Used:

Python-Backend language                       
Flask - Lightweight web framework              
HTML/CSS-Page layout & styling                  
JavaScript (basic)-Form interactivity (checkboxes, input) 

File Structure
app.py         # Main Flask application (runs the server)
README.md      # Project overview and usage guide
(Note: HTML, CSS, and JS are embedded inside `app.py` using `render_template_string()`)

 Getting Started:

1. Install Python

Make sure Python 3 is installed:

bash
python --version

2. Install Flask

Install Flask using pip:

bash
pip install flask


 3. Run the App

Save the code in `app.py`, then run:

bash
python app.py



Screenshots

Booking form: ![Form](https://via.placeholder.com/400x200.png?text=Booking+Form) 
Flash message:![Success](https://via.placeholder.com/400x200.png?text=Booking+Success) 



 Notes

* This is a **demo app** with in-memory storage — bookings reset when the app restarts.
* Payment is **simulated**; no real transactions occur.
* Each booking gets a unique ID (e.g., `B001`, `B002`).
