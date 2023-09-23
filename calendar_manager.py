import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from tkcalendar import Calendar
from datetime import datetime

def save_event():
    date = cal.get_date()
    event = event_entry.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    
    if all([date, event]):
        with open('data/resources.txt', 'a') as file:
            file.write(" \n")
            file.write(f"Date: {date}, Event: {event}\nStart Time: {start_time}\nEnd Time: {end_time}\n")
            file.write(" \n")
            file.write("========================\n")

        event_entry.delete(0, tk.END)
        start_time_entry.delete(0, tk.END)
        end_time_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Event saved successfully.")
    else:
        messagebox.showerror("Error", "Date and Event are required fields.")

def show_events():
    try:
        with open('data/resources.txt', 'r') as file:
            events = file.read()
            messagebox.showinfo("Saved Events", events)
    except FileNotFoundError:
        messagebox.showerror("Error", "You have no events saved yet.")

def show_calendar_events(event):
    date = cal.get_date()
    try:
        with open('data/resources.txt', 'r') as file:
            events = file.readlines()
            event_details = ""
            for event_line in events:
                if f"Date: {date}" in event_line:
                    event_details += event_line + "\n"
            if event_details:
                event_details = event_details.strip()
                messagebox.showinfo("Events on Date", event_details)
            else:
                messagebox.showinfo("No Events", "No events found for this date.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No events found.")

root = tk.Tk()
root.title("Calendar Event Manager")

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.mkdir('data')

cal = Calendar(root)
cal.pack(padx=10, pady=10)

event_label = tk.Label(root, text="Event:")
event_label.pack(pady=(0, 5))

event_entry = tk.Entry(root, width=30)
event_entry.pack(pady=5)

start_time_label = tk.Label(root, text="Start Time (HH:MM):")
start_time_label.pack(pady=(0, 5))

start_time_entry = tk.Entry(root, width=10)
start_time_entry.pack(pady=5)

end_time_label = tk.Label(root, text="End Time (HH:MM):")
end_time_label.pack(pady=(0, 5))

end_time_entry = tk.Entry(root, width=10)
end_time_entry.pack(pady=5)

save_button = tk.Button(root, text="Save Event", command=save_event)
save_button.pack(pady=10)

show_button = tk.Button(root, text="Show Events", command=show_events)
show_button.pack(pady=10)

cal.bind("<ButtonRelease-1>", show_calendar_events)

root.geometry("400x475")  # Ustawienie początkowych wymiarów okna
root.resizable(False, False)  # Uniemożliwienie zmiany rozmiaru okna
root.update_idletasks()  # Aktualizacja okna

# Wycentrowanie okna na środku ekranu
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - root.winfo_reqwidth()) // 2
y_coordinate = (screen_height - root.winfo_reqheight()) // 2
root.geometry("+{}+{}".format(x_coordinate, y_coordinate))

root.mainloop()
