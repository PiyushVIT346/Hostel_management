import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk module for Notebook
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('hostel.db')
cursor = conn.cursor()

# Create the tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        roll_no TEXT,
        room_no INTEGER,
        hostel TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        room_no INTEGER,
        capacity INTEGER,
        hostel TEXT
    )
''')

conn.commit()

# Function to add a new student
def add_student():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    room_no = room_no_entry.get()
    hostel = hostel_entry.get()

    if not name or not roll_no or not room_no or not hostel:
        messagebox.showerror('Input Error', 'Please fill out all fields.')
        return

    cursor.execute('''
        INSERT INTO students (name, roll_no, room_no, hostel)
        VALUES (?, ?, ?, ?)
    ''', (name, roll_no, room_no, hostel))
    conn.commit()
    messagebox.showinfo('Success', 'Student added successfully!')

# Function to add a new room
def add_room():
    room_no = room_no_entry_room.get()
    capacity = capacity_entry.get()
    hostel = hostel_entry_room.get()

    if not room_no or not capacity or not hostel:
        messagebox.showerror('Input Error', 'Please fill out all fields.')
        return

    cursor.execute('''
        INSERT INTO rooms (room_no, capacity, hostel)
        VALUES (?, ?, ?)
    ''', (room_no, capacity, hostel))
    conn.commit()
    messagebox.showinfo('Success', 'Room added successfully!')

# Function to search for a student
def search_student():
    roll_no = search_roll_no_entry.get()
    cursor.execute('''
        SELECT * FROM students WHERE roll_no = ?
    ''', (roll_no,))
    student = cursor.fetchone()

    if student:
        messagebox.showinfo('Student Found', f'Name: {student[1]}\nRoom No: {student[3]}\nHostel: {student[4]}')
    else:
        messagebox.showinfo('Not Found', 'Student not found!')

# Function to exit the application
def exit_app():
    root.quit()

# Create the GUI
root = tk.Tk()
root.title('Hostel Management Software')

# Set window size
root.geometry("500x700")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Style configurations
card_bg = "#ffffff"  # Card background color
btn_bg = "#4CAF50"    # Button background color
btn_fg = "white"      # Button text color
card_border_color = "#cccccc"  # Card border color

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Add Student Tab
add_student_tab = ttk.Frame(notebook)
notebook.add(add_student_tab, text='Add Student')

tk.Label(add_student_tab, text='Add Student', bg=card_bg, font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(add_student_tab, text='Name:', bg=card_bg).grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(add_student_tab)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(add_student_tab, text='Roll No:', bg=card_bg).grid(row=2, column=0, padx=10, pady=5)
roll_no_entry = tk.Entry(add_student_tab)
roll_no_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(add_student_tab, text='Room No:', bg=card_bg).grid(row=3, column=0, padx=10, pady=5)
room_no_entry = tk.Entry(add_student_tab)
room_no_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(add_student_tab, text='Hostel:', bg=card_bg).grid(row=4, column=0, padx=10, pady=5)
hostel_entry = tk.Entry(add_student_tab)
hostel_entry.grid(row=4, column=1, padx=10, pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app, bg="#FF0000", fg="white")
exit_button.pack(pady=200,padx=1)

tk.Button(add_student_tab, text='Add Student', command=add_student, bg=btn_bg, fg=btn_fg).grid(row=5, column=0, columnspan=2, pady=10)

# Add Room Tab
add_room_tab = ttk.Frame(notebook)
notebook.add(add_room_tab, text='Add Room')

tk.Label(add_room_tab, text='Add Room', bg=card_bg, font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(add_room_tab, text='Room No:', bg=card_bg).grid(row=1, column=0, padx=10, pady=5)
room_no_entry_room = tk.Entry(add_room_tab)
room_no_entry_room.grid(row=1, column=1, padx=10, pady=5)

tk.Label(add_room_tab, text='Capacity:', bg=card_bg).grid(row=2, column=0, padx=10, pady=5)
capacity_entry = tk.Entry(add_room_tab)
capacity_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(add_room_tab, text='Hostel:', bg=card_bg).grid(row=3, column=0, padx=10, pady=5)
hostel_entry_room = tk.Entry(add_room_tab)
hostel_entry_room.grid(row=3, column=1, padx=10, pady=5)

tk.Button(add_room_tab, text='Add Room', command=add_room, bg=btn_bg, fg=btn_fg).grid(row=4, column=0, columnspan=2, pady=10)

# Search Student Tab
search_student_tab = ttk.Frame(notebook)
notebook.add(search_student_tab, text='Search Student')

tk.Label(search_student_tab, text='Search Student', bg=card_bg, font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(search_student_tab, text='Roll No:', bg=card_bg).grid(row=1, column=0, padx=10, pady=5)
search_roll_no_entry = tk.Entry(search_student_tab)
search_roll_no_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(search_student_tab, text='Search', command=search_student, bg=btn_bg, fg=btn_fg).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
