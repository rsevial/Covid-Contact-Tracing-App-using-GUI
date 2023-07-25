# Programmed by: Rebekah Joy E. Sevial
# The program will execute the created GUI app

# Import all class and module
from contact_tracing_gui import ContactTracingGUI
from tkinter import *
# Constructor that will make the main window of the app
main = Tk()
# Making what we created in GUI as objects
contact_tracing_gui = ContactTracingGUI(main)
# Execute the GUI app
main.mainloop()