import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class MovieTicketBookingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 Movie Ticket Booking System")
        self.movies = {
            "Inception": 10,
            "Interstellar": 8,
            "The Matrix": 5
        }
        self.bookings = {}
        self.food_menu = {
            "Popcorn": 100,
            "Coke": 50,
            "Nachos": 120
        }

        self.create_main_menu()

    def create_main_menu(self):
        tk.Label(self.root, text="Welcome to Movie Booking System", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="🎟️ Book Ticket", width=25, command=self.book_ticket).pack(pady=5)
        tk.Button(self.root, text="❌ Cancel Ticket", width=25, command=self.cancel_ticket).pack(pady=5)
        tk.Button(self.root, text="👋 Exit", width=25, command=self.root.quit).pack(pady=5)

    def book_ticket(self):
        movie = self.ask_movie()
        if not movie:
            return

        try:
            seats = int(simpledialog.askstring("Seats", f"Enter number of tickets (Available: {self.movies[movie]}):"))
        except:
            return

        if seats > self.movies[movie]:
            messagebox.showerror("Error", "Not enough seats available!")
            return

        name = simpledialog.askstring("Name", "Enter your name:")
        if not name:
            return

        food_items, food_cost = self.order_food()
        total_cost = seats * 150 + food_cost

        if not self.payment_gateway(total_cost):
            return

        self.movies[movie] -= seats
        booking_id = str(random.randint(1000, 9999))
        self.bookings[booking_id] = {
            "name": name,
            "movie": movie,
            "seats": seats,
            "food": food_items,
            "total": total_cost
        }

        messagebox.showinfo("Success", f"✅ Booking Successful!\nBooking ID: {booking_id}")

    def ask_movie(self):
        movie_window = tk.Toplevel(self.root)
        movie_window.title("Select Movie")
        selected = tk.StringVar()

        tk.Label(movie_window, text="Select a movie:", font=("Arial", 12)).pack(pady=10)
        for movie in self.movies:
            tk.Radiobutton(movie_window, text=f"{movie} ({self.movies[movie]} seats)", variable=selected, value=movie).pack(anchor="w")

        def confirm():
            movie_window.destroy()

        tk.Button(movie_window, text="OK", command=confirm).pack(pady=10)
        movie_window.wait_window()
        return selected.get()

    def order_food(self):
        food_window = tk.Toplevel(self.root)
        food_window.title("Order Food")
        selected_items = {}
        vars = {}

        tk.Label(food_window, text="🍔 Select Food Items:", font=("Arial", 12)).pack(pady=10)

        for item, price in self.food_menu.items():
            var = tk.IntVar()
            chk = tk.Checkbutton(food_window, text=f"{item} - ₹{price}", variable=var)
            chk.pack(anchor="w")
            vars[item] = var

        def confirm():
            food_window.destroy()

        tk.Button(food_window, text="Done", command=confirm).pack(pady=10)
        food_window.wait_window()

        selected = []
        total = 0
        for item, var in vars.items():
            if var.get():
                selected.append(item)
                total += self.food_menu[item]
        return selected, total

    def payment_gateway(self, amount):
        msg = f"💳 Total Amount: ₹{amount}\nProceed to payment?"
        if not messagebox.askyesno("Payment", msg):
            return False

        card = simpledialog.askstring("Payment", "Enter 16-digit card number:")
        cvv = simpledialog.askstring("Payment", "Enter 3-digit CVV:")
        if card and cvv and len(card) == 16 and len(cvv) == 3:
            messagebox.showinfo("Payment", "✅ Payment Successful!")
            return True
        else:
            messagebox.showerror("Payment Failed", "❌ Invalid card details.")
            return False

    def cancel_ticket(self):
        booking_id = simpledialog.askstring("Cancel Ticket", "Enter Booking ID:")
        if booking_id in self.bookings:
            movie = self.bookings[booking_id]["movie"]
            self.movies[movie] += self.bookings[booking_id]["seats"]
            del self.bookings[booking_id]
            messagebox.showinfo("Cancelled", "✅ Ticket Cancelled Successfully.")
        else:
            messagebox.showerror("Error", "❌ Invalid Booking ID.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MovieTicketBookingGUI(root)
    root.mainloop()
