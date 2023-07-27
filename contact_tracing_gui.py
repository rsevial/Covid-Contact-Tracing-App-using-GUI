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
        add_window.geometry("450x700")
        add_window.configure(bg="white")
        
        # Create variable for font and size that you will use often.
        child_window_title_font = Font(family="Montserrat", size=20, weight="bold")
        child_window_font_for_ques = ("Oxygen Bold", 12)
        child_window_label_font = Font(family="Montserrat", size=13, weight="bold")
        
        # Put a heading for add record
        add_frame = Frame(add_window, bg="white")
        add_frame.pack(padx=10, pady=25)
        new_con = Label(add_frame, text="New Record", bg="#1b5886", fg="white", width=25, height=1, font=child_window_title_font)
        new_con.grid(row=0, columnspan=1, sticky="w", pady=8)
        
        # Provide a instruction for the user to keep
        instructions = Label(add_frame, text="Kindly respond to the following questions with utmost honesty:", fg="#152238", bg="white", height=1, font=child_window_font_for_ques)
        instructions.grid(row=1, columnspan=1, sticky="w", pady=3, padx=3)

        # Create a section named Respondent Details
        res_details = Label(add_frame, text="Respondent Details", fg="#007fff", bg="white", height=1, font=child_window_label_font)
        res_details.grid(row=2, columnspan=1, sticky="w", pady=3, padx=3)     
        
        # Create checkbutton, text, entry for asking the user's 
        # name
        name_label = Label(add_frame, text="1. Full Name", fg="#152238", bg="white", font=child_window_label_font)
        name_label.grid(row=3, column=0, pady=3, padx= 1, sticky="w")
        
        # first name
        first_name_label = Label(add_frame, text="Last Name:", fg="#152238", bg="white", font=child_window_font_for_ques)
        first_name_label.grid(row=4, column=0, pady=3, padx= 1, sticky="w")
        self.last_name_entry = Entry(add_frame)
        self.last_name_entry.grid(row=4, columnspan=1, sticky="e")
        
        # last name
        first_name_label = Label(add_frame, text="First Name:", fg="#152238", bg="white", font=child_window_font_for_ques)
        first_name_label.grid(row=5, column=0, pady=3, padx= 1, sticky="w")
        self.first_name_entry = Entry(add_frame)
        self.first_name_entry.grid(row=5, columnspan=1, sticky="e")
        
        # address
        address_label = Label(add_frame, text="2. Address:", fg="#152238", bg="white", font=child_window_label_font)
        address_label.grid(row=6, column=0, pady=3, padx=1, sticky="w")
        self.address_entry = Text(add_frame, width=48, height=2)
        self.address_entry.grid(row=7, column=0, sticky="w")
        
        # Contact Number
        contact_number_label = Label(add_frame, text="3. Contact Number:", fg="#152238", bg="white", font=child_window_label_font)
        contact_number_label.grid(row=9, column=0, pady=3, padx= 1, sticky="w")
        self.contact_number_entry = Entry(add_frame)
        self.contact_number_entry.grid(row=9, columnspan=1, sticky="e")
        
        # email
        email_label = Label(add_frame, text="4. Email Address:", fg="#152238", bg="white", font=child_window_label_font)
        email_label.grid(row=10, column=0, pady=3, padx= 1, sticky="w")
        self.email_label_entry = Entry(add_frame)
        self.email_label_entry.grid(row=10, columnspan=1, sticky="e")
        
        # vaccine
        vaccine_label = Label(add_frame, text="5. Have you been vaccinated for COVID-19?", fg="#152238", bg="white", font=child_window_label_font)
        vaccine_label.grid(row=11, columnspan=1, pady=3, padx= 1, sticky="w")
        self.vaccine_var = StringVar()
        self.vaccine_var.set("Not yet")
        vaccine_choices = ["Not yet", "1st Dose", "2nd Dose(Fully Vaccinated)", "1st Booster Shot"]
        for i in range(len(vaccine_choices)):
            vaccine = vaccine_choices[i]
            radiobutton = Radiobutton(add_frame, text=vaccine, variable=self.vaccine_var, value=vaccine,fg="#152238", bg="white", font=child_window_font_for_ques)
            radiobutton.grid(row=12+i, column=0, columnspan=1, sticky="w")
        
        # Create a section Respondent Details
        contact_per_details = Label(add_frame, text="Contact Person Details", fg="#007fff", bg="white", height=1, font=child_window_label_font)
        contact_per_details.grid(row=16, columnspan=1, sticky="w", pady=3, padx=3) 

        # contact_person_name
        contact_person_name_label = Label(add_frame, text="6.a Name:", fg="#152238", bg="white", font=child_window_label_font)
        contact_person_name_label.grid(row=17, column=0, pady=3, padx= 1, sticky="w")
        self.contact_person_name_label_entry = Entry(add_frame)
        self.contact_person_name_label_entry.grid(row=17, columnspan=1, sticky="e")
       
        #  contact_person_phone
        contact_person_phone_label = Label(add_frame, text="6.b Contact Number:", fg="#152238", bg="white", font=child_window_label_font)
        contact_person_phone_label.grid(row=18, column=0, pady=3, padx= 1, sticky="w")
        self.contact_person_phone_entry = Entry(add_frame)
        self.contact_person_phone_entry.grid(row=18, columnspan=1, sticky="e")

    # Def function that will to get the data entered
    def add_record_action(self):
        last_name = self.last_name_entry.get()
        first_name = self.first_name_entry.get()
        address = self.address_entry.get()
        contact_number = self.contact_number_entry.get()
        email = self.email_label_entry.get
        vaccine = self.vaccine_var.get()
        contact_person_name = self.contact_person_name_label_entry.get()
        contact_person_phone = self.contact_person_phone_entry.get()
    
    # Def functions that will display a child window named search if the user picks search buttons
        # Create a child window
        # Create search key that will ask the name of the user

