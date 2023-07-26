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
        # Put a heading to welcome the user and will ask the if he/she will add entry or search contacts
        # Create and state the position for add and search entry buttons
    # Def functions that will display a child window named add if the user picks add buttons
        # Create a child window
        # Create checkbutton, text, entry for asking the user's 
        # name, address, contact_number, email, vaccine, vaccine_result, contact_person_name, contact_person_phone
    # Def functions that will display a child window named search if the user picks search buttons
        # Create a child window
        # Create search key that will ask the name of the user