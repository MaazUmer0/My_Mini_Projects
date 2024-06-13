import tkinter as tk
from tkinter import messagebox

# Define the menu with prices
menu = {
    "Burger": 400,
    "Pizza": 600,
    "Pasta": 500,
    "Roll": 250,
    "Sandwich": 300,
    "Handi": 1200,
    "Biryani": 800,
    "Rice": 200,
    "Noodles": 300,
    "Soup": 100,
    "Salad": 150,
    "Bread": 50,
    "Drink": 100,
    "Dessert": 200,
}

# Function to add items to the order list and update the total cost
def add_to_order():
    item = item_var.get()
    if item in menu:
        order_listbox.insert(tk.END, item)
        total_cost_var.set(total_cost_var.get() + menu[item])
    else:
        messagebox.showerror("Error", f"Item '{item}' not found in the menu.")

# Function to finalize the order and display the bill
def finalize_order():
    order_items = order_listbox.get(0, tk.END)
    if not order_items:
        messagebox.showerror("Error", "No items in the order.")
        return

    total_cost = total_cost_var.get()
    bill = "Your Order Receipt:\n\n"
    for item in order_items:
        bill += f"{item}: Rs{menu[item]}\n"
    bill += f"\nTotal cost: Rs{total_cost}"
    messagebox.showinfo("Bill", bill)

# Function to display the menu
def display_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")
    
    menu_listbox = tk.Listbox(menu_window, height=15, width=40)
    for item, price in menu.items():
        menu_listbox.insert(tk.END, f"{item}: Rs{price}")
    menu_listbox.pack(pady=10)

# Setting up the main window
root = tk.Tk()
root.title("Hotel Order System")

# Setting up the item entry and add button
item_label = tk.Label(root, text="Enter item to order:")
item_label.pack(pady=5)
item_var = tk.StringVar()
item_entry = tk.Entry(root, textvariable=item_var)
item_entry.pack(pady=5)
add_button = tk.Button(root, text="Add to Order", command=add_to_order)
add_button.pack(pady=5)

# Setting up the order listbox and scrollbar
order_label = tk.Label(root, text="Order List:")
order_label.pack(pady=5)
order_frame = tk.Frame(root)
order_scrollbar = tk.Scrollbar(order_frame, orient=tk.VERTICAL)
order_listbox = tk.Listbox(order_frame, height=10, width=30, yscrollcommand=order_scrollbar.set)
order_scrollbar.config(command=order_listbox.yview)
order_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
order_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
order_frame.pack(pady=5)

# Setting up the total cost display
total_cost_label = tk.Label(root, text="Total Cost:")
total_cost_label.pack(pady=5)
total_cost_var = tk.IntVar(value=0)
total_cost_display = tk.Label(root, textvariable=total_cost_var)
total_cost_display.pack(pady=5)

# Setting up the finalize order button
finalize_button = tk.Button(root, text="Finalize Order", command=finalize_order)
finalize_button.pack(pady=20)

# Setting up the menu display button
menu_button = tk.Button(root, text="Show Menu", command=display_menu)
menu_button.pack(pady=10)

# Running the application
root.mainloop()
