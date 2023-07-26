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
        # Put a heading to welcome the user and will ask the if he/she will add entry or search contacts
        window.heading = Label(text="Contact Tracing for COVID-19", fg="white", bg="#1b5886", width=30, height=2, font=window.title_font)
        window.heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        window.greet = Label(text="Please select the desired method of operation.", fg="#1b5886", bg="white", width=40, height=1,  font=window.label_font)
        window.greet.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")
        # Create and state the position for add and search entry buttons
        # for add entry
        window.add_button = Button(master=main, text="Add Record | +", width=15, height=2, fg="#003a88", bg="#90b1db", relief=GROOVE, font=window.label_font, justify="left")
        window.add_button.grid(row=3, column=0, padx=10, pady=10)
        # for search entry
    # Def functions that will display a child window named add if the user picks add buttons
        # Create a child window
        # Create checkbutton, text, entry for asking the user's 
        # name, address, contact_number, email, vaccine, vaccine_result, contact_person_name, contact_person_phone
    # Def functions that will display a child window named search if the user picks search buttons
        # Create a child window
        # Create search key that will ask the name of the user