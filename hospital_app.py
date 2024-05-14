import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog
from user_authentication import UserAuthentication
from patient_record_manager import PatientRecordManager
from patient_record import PatientRecord

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("600x500")

        # Styling
        self.root.configure(bg="#f0f0f0")
        self.label_font = ("Helvetica", 12)
        self.entry_font = ("Helvetica", 12)

        self.user_authenticator = UserAuthentication("PA3_credentials.csv")
        self.patient_manager = None
        self.current_user = None

        self.login_frame = tk.Frame(root)
        self.login_frame.pack(pady=20)

        self.username_label = tk.Label(self.login_frame, text="Username:", font=self.label_font, bg="#f0f0f0")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.username_entry = tk.Entry(self.login_frame, font=self.entry_font)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:", font=self.label_font, bg="#f0f0f0")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = tk.Entry(self.login_frame, show="*", font=self.entry_font)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = tk.Button(self.login_frame, text="Login", font=self.label_font, command=self.login, bg="#4CAF50", fg="white", relief="raised", borderwidth=3)
        self.login_button.grid(row=2, columnspan=2, pady=10)

         # Check if the usage log file exists
        if not os.path.exists("usage_log.csv"):
            # If it doesn't exist, create the file and write the header row
            with open("usage_log.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Username", "Role", "Action", "Timestamp"])

        # Open the usage statistics file in append mode
        self.usage_log_file = open("usage_log.csv", "a", newline="")
        self.usage_log_writer = csv.writer(self.usage_log_file)

    def log_usage(self, action):
        # Log the usage statistics with relevant information
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.usage_log_writer.writerow([self.current_user, self.current_role, action, timestamp])
        self.usage_log_file.flush()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        role = self.user_authenticator.authenticate_user(username, password)

        if role is None:
            messagebox.showerror("Error", "Invalid credentials.")
        else:
            self.current_user = username
            self.current_role = role
            self.patient_manager = PatientRecordManager("PA3_patients.csv")
            self.login_frame.destroy()
            self.show_menu(role)

    def show_menu(self, role):
        # Styling
        menu_bg_color = "#f0f0f0"
        label_bg_color = "#4CAF50"
        label_fg_color = "white"
        label_font = ("Helvetica", 12, "bold")
        button_bg_color = "#4CAF50"
        button_fg_color = "white"
        button_font = ("Helvetica", 10)
        button_relief = "raised"
        button_border_width = 3
        button_width = 20
        button_height = 2
        pady = 10

        self.menu_frame = tk.Frame(self.root, bg=menu_bg_color)
        self.menu_frame.pack(pady=20)

        welcome_label_text = "Welcome! You are logged in as " + role
        self.welcome_label = tk.Label(self.menu_frame, text=welcome_label_text, bg=label_bg_color, fg=label_fg_color, font=label_font, pady=10)
        self.welcome_label.pack(fill="x")

        if role == "management":
            self.key_stats_button = tk.Button(self.menu_frame, text="Generate Key Statistics", command=self.generate_key_statistics, bg=button_bg_color, fg=button_fg_color, font=button_font, relief=button_relief, borderwidth=button_border_width, width=button_width, height=button_height)
            self.key_stats_button.pack(pady=pady)
    
        elif role == "admin":
            self.count_visits_button = tk.Button(self.menu_frame, text="Count Visits", command=self.count_visits, bg=button_bg_color, fg=button_fg_color, font=button_font, relief=button_relief, borderwidth=button_border_width, width=button_width, height=button_height)
            self.count_visits_button.pack(pady=pady)

        elif role in ["nurse", "clinician"]:
            self.retrieve_patient_button = tk.Button(self.menu_frame, text="Retrieve Patient", command=self.retrieve_patient, bg=button_bg_color, fg=button_fg_color, font=button_font, relief=button_relief, borderwidth=button_border_width, width=button_width, height=button_height)
            self.retrieve_patient_button.pack(pady=pady)

            self.add_patient_button = tk.Button(self.menu_frame, text="Add Patient", command=self.add_patient, bg=button_bg_color, fg=button_fg_color, font=button_font, relief=button_relief, borderwidth=button_border_width, width=button_width, height=button_height)
            self.add_patient_button.pack(pady=pady)

            self.remove_patient_button = tk.Button(self.menu_frame, text="Remove Patient", command=self.remove_patient, bg=button_bg_color, fg=button_fg_color, font=button_font, relief=button_relief, borderwidth=button_border_width, width=button_width, height=button_height)
            self.remove_patient_button.pack(pady=pady)

            self.count_visits_button = tk.Button(self.menu_frame, text="Count Visits", command=self.count_visits, bg=button_bg_color, fg=button_fg_color, font=button_font, relief=button_relief, borderwidth=button_border_width, width=button_width, height=button_height)
            self.count_visits_button.pack(pady=pady)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=self.root.destroy, bg=button_bg_color, fg=button_fg_color, font=button_font, relief=button_relief, borderwidth=button_border_width, width=button_width, height=button_height)
        self.exit_button.pack(pady=pady)

    def generate_key_statistics(self):
        self.patient_manager.generate_key_statistics()
        messagebox.showinfo("Info", "Key statistics generated.",parent=self.root)
        # Log usage 
        self.log_usage("Generate Statistics")

    def retrieve_patient(self):
        patient_id = simpledialog.askstring("Input", "Enter Patient ID:", parent=self.root)
        if patient_id is not None:
            patient_record = self.patient_manager.retrieve_patient_record(patient_id)
            if patient_record:
                messagebox.showinfo("Patient Information", patient_record,parent=self.root)
            else:
                messagebox.showerror("Error", "Patient not found.",parent=self.root)
        # Log usage 
        self.log_usage("Retrieve Patient")

    def add_patient(self):
        # Create a new window for adding a patient
        self.add_patient_window = Toplevel(self.root)
        self.add_patient_window.title("Add Patient")
        self.add_patient_window.geometry("500x500")

        # Styling
        label_bg_color = "#f0f0f0"
        entry_bg_color = "white"
        entry_font = ("Helvetica", 10)
        padx = 10
        pady = 5

        labels = [
            "Patient ID:", "Visit ID:", "Visit Time (yyyy-mm-dd):", "Visit Department:",
            "Gender:", "Race:", "Age:", "Ethnicity:", "Insurance:", "Zip Code:",
            "Chief Complaint:", "Note ID:", "Note Type:"
        ]

        self.entries = []  # List to store Entry widgets

        for i, label_text in enumerate(labels):
            label = Label(self.add_patient_window, text=label_text, bg=label_bg_color)
            label.grid(row=i, column=0, padx=padx, pady=pady, sticky="w")

            entry = Entry(self.add_patient_window, bg=entry_bg_color, font=entry_font)
            entry.grid(row=i, column=1, padx=padx, pady=pady)
            self.entries.append(entry)  # Add Entry widget to the list

        # Button to submit patient information
        self.submit_button = Button(self.add_patient_window, text="Submit", command=self.submit_patient_info)
        self.submit_button.grid(row=13, column=1, padx=10, pady=10)

        # Log usage 
        self.log_usage("Add Patient")

    def submit_patient_info(self):
        # Retrieve patient information from entry widgets
        patient_id = self.entries[0].get()
        visit_id = self.entries[1].get()
        visit_time = self.entries[2].get()
        visit_department = self.entries[3].get()
        gender = self.entries[4].get()
        race = self.entries[5].get()
        age = self.entries[6].get()
        ethnicity = self.entries[7].get()
        insurance = self.entries[8].get()
        zip_code = self.entries[9].get()
        chief_complaint = self.entries[10].get()
        note_id = self.entries[11].get()
        note_type = self.entries[12].get()

        # Call add_patient_record method of PatientRecordManager
        patient_record = PatientRecord(patient_id, visit_id, visit_time, visit_department, gender, race, age, ethnicity, insurance, zip_code, chief_complaint, note_id, note_type)
        self.patient_manager.add_patient_record(patient_record)

        # Show success message
        messagebox.showinfo("Success", "Patient added successfully.",parent=self.root)

    def remove_patient(self):
        patient_id = simpledialog.askstring("Input", "Enter Patient ID:",parent=self.root)
        if patient_id is not None:
            if self.patient_manager.remove_patient_record(patient_id):
                messagebox.showinfo("Info", "Patient removed successfully.",parent=self.root)
            else:
                messagebox.showerror("Error", "Patient not found.",parent=self.root)
        
        # Log usage
        self.log_usage("Remove Patient")

    def count_visits(self):
        date_str = simpledialog.askstring("Input", "Enter the date (yyyy-mm-dd):",parent=self.root)
        if date_str is not None:
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                total_visits = self.patient_manager.count_visits_on_date(date)
                messagebox.showinfo("Visits Count", f"Total visits on {date_str}: {total_visits}",parent=self.root)
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please enter date in yyyy-mm-dd format.",parent=self.root)
        
        # Log usage 
        self.log_usage("Count Visits")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
