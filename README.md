Movie Ticket Booking system

This is a graphical desktop application built using Python and Tkinter. The system allows users to book movie tickets, order food, and simulate a payment process within a simple GUI interface. It is ideal for beginner to intermediate Python learners looking to understand GUI design and event-driven programming.

Features
GUI built with Tkinter (no web development required)

Displays available movies and remaining seats

Allows ticket booking with seat selection

Supports optional food ordering with prices

Includes basic payment simulation (card and CVV input)

Generates a unique booking ID for each transaction

Provides ticket cancellation by Booking ID

Technologies Used
Python 3

Tkinter (standard GUI library in Python)

random module for generating booking IDs

Prerequisites
Python 3 must be installed on your system

No external libraries are required (Tkinter is included with Python)

How to Run
Save the code to a file, for example: movie_booking_gui.py

Open a terminal or command prompt in the directory containing the file

Run the script using:

nginx
Copy
Edit
python movie_booking_gui.py
The graphical user interface will appear and guide you through the booking process

Application Workflow
Home Screen
The main menu provides three options: Book Ticket, Cancel Ticket, and Exit.

Booking Process

The user selects a movie from the available list

Specifies the number of tickets

Optionally selects food items from a menu

Provides simulated card payment information (card number and CVV)

If payment is successful, a booking confirmation with a unique ID is displayed

Cancel Ticket

The user enters their booking ID

If valid, the booking is canceled and seat count is updated

Notes
This is a demo system; no real payments are processed

All data is stored in memory during runtime and will be lost once the program is closed

The UI is styled using Tkinter's built-in widget properties, not CSS

Future Enhancements
Persist booking data to a local file or SQLite database

Add user login or profile tracking

Export ticket details as a printable file

Add a real-time seat selection grid
