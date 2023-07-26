# Programmed by: Rebekah Joy E. Sevial
# Contact Tracing using GUI

# Import all the needed modules and class from other class
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from contact_tracing_app import ContactTracingApp

# Create a class named ContactTracingGUI
class ContactTracingGUI:
    # Def function for main window
    def __init__(self,main):
        self.contact_tracing_app = ContactTracingApp
        self.main = main
        window = self.main
        # Create a Title for parent window
        window.title("Contact Tracing Application")
        # Create a frame and the preferred size and color of the parent window
        window.geometry("625x300")
        window.configure(bg="white") 
        # Create variable for font and size that you will use often.
        window.title_font = Font(family="Century Gothic", size=25, weight="bold")
        window.label_font = ("Montserrat", 12)
        window.font_for_ques = ("Oxygen Bold", 11)
        # Put a heading to welcome the user and will ask the if he/she will add entry or search contacts
        window.heading = Label(text="Contact Tracing for COVID-19", fg="white", bg="#1b5886", width=30, height=2, font=window.title_font)
        window.heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        window.greet = Label(text="Please select the desired method of operation.", fg="#1b5886", bg="white", width=40, height=1,  font=window.label_font)
        window.greet.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")
        # Create and state the position for add and search entry buttons
        # for add entry
        window.add_button = Button(master=main, text="Add Record | +", width=15, height=2, fg="#003a88", bg="#90b1db", relief=GROOVE, font=window.label_font, justify="left", command=self.add_record)
        window.add_button.grid(row=3, column=0, padx=10, pady=10)
        # for search entry
        window.search_button = Button(master=main, text="Search Record", width=15, height=2, fg="#003a88", bg="#90b1db", relief=GROOVE, font=window.label_font, justify="right")
        window.search_button.grid(row=3, column=1, padx=10, pady=10)
    # Def functions that will display a child window named add if the user picks add buttons
    def add_record(self):
        # Create a child window
        add_window = Toplevel(self.main)
        add_window.title("Add Record")
        add_window.geometry("600x700")
        add_window.configure(bg="white")
        # Create variable for font and size that you will use often.
        child_window_title_font = Font(family="Montserrat", size=20, weight="bold")
        child_window_font_for_ques = ("Oxygen Bold", 11)
        child_window_label_font = Font(family="Montserrat", size=11, weight="bold")
        # Put a heading for add record
        add_frame = Frame(add_window, bg="white")
        add_frame.pack(padx=10, pady=25)
        new_con = Label(add_frame, text="New Record", bg="#1b5886", fg="white", width=35, height=1, font=child_window_title_font)
        new_con.grid(row=0, columnspan=3, sticky="w", pady=10)
        # Provide a instruction for the user to keep
        instructions = Label(add_frame, text="Kindly respond to the following questions with utmost honesty:", fg="#152238", bg="white", height=1, font=child_window_font_for_ques)
        instructions.grid(row=1, columnspan=3, sticky="w", pady=3, padx=3)     
        # Create checkbutton, text, entry for asking the user's 
        # name
        name_label = Label(add_frame, text="1. Full Name", fg="#152238", bg="white", font=child_window_label_font)
        name_label.grid(row=2, column=0, pady=3, padx= 1, sticky="w")
        
        first_name_label = Label(add_frame, text="Last Name:", fg="#152238", bg="white", font=child_window_font_for_ques)
        first_name_label.grid(row=3, column=0, pady=3, padx= 1, sticky="w")
        self.last_name_entry = Entry(add_frame)
        self.last_name_entry.grid(row=3, column=1, sticky="w")

        first_name_label = Label(add_frame, text="First Name:", fg="#152238", bg="white", font=child_window_font_for_ques)
        first_name_label.grid(row=4, column=0, pady=3, padx= 1, sticky="w")
        self.first_name_entry = Entry(add_frame)
        self.first_name_entry.grid(row=4, column=1, sticky="w")
        # address
        address_label = Label(add_frame, text="2. Address:", fg="#152238", bg="white", font=child_window_label_font)
        address_label.grid(row=5, column=0, pady=3, padx=1, sticky="w")
        self.address_entry = Entry(add_frame)
        self.address_entry.grid(row=5, column=1, sticky="w")
        # contact_number, email, vaccine, vaccine_result, contact_person_name, contact_person_phone
    # Def function that will to get the data entered
    def add_record_action(self):
        name = self.name_entry.get()
        address = self.address_entry.get()

    # Def functions that will display a child window named search if the user picks search buttons
        # Create a child window
        # Create search key that will ask the name of the user