# Import all the needed modules and class from other class
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkinter import ttk
from contact_tracing_app import ContactTracingApp, ContactTracingRecords

# Create a class named ContactTracingGUI
class ContactTracingGUI:
    # Def function for main window
    def __init__(self,main):
        self.contact_tracing_app = ContactTracingApp("contact_tracing_records.txt")
        self.main = main
        window = self.main
        self.match_entry = []

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
        window.search_button = Button(master=main, text="Search Record", width=15, height=2, fg="#003a88", bg="#90b1db", relief=GROOVE, font=window.label_font, justify="right", command=self.search_record)
        window.search_button.grid(row=3, column=1, padx=10, pady=10)
        
        # Center the window on the screen.
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - window.winfo_width()) // 2
        y = (screen_height - window.winfo_height()) // 2
        window.geometry('+{}+{}'.format(x, y))

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
        respondents_details = Label(add_frame, text="Respondent Details", fg="#007fff", bg="white", height=1, font=child_window_label_font)
        respondents_details.grid(row=2, columnspan=1, sticky="w", pady=3, padx=3)     
        
        # Create checkbutton, text, entry for asking the user's 
        # name
        name_label = Label(add_frame, text="1. Full Name", fg="#152238", bg="white", font=child_window_label_font)
        name_label.grid(row=3, column=0, pady=3, padx= 1, sticky="w")
        
        # last name
        last_name_label = Label(add_frame, text="Last Name:", fg="#152238", bg="white", font=child_window_font_for_ques)
        last_name_label.grid(row=4, column=0, pady=3, padx= 1, sticky="w")
        self.last_name_entry = Entry(add_frame)
        self.last_name_entry.grid(row=4, columnspan=1, sticky="e")
        
        # first name
        first_name_label = Label(add_frame, text="First Name:", fg="#152238", bg="white", font=child_window_font_for_ques)
        first_name_label.grid(row=5, column=0, pady=3, padx= 1, sticky="w")
        self.first_name_entry = Entry(add_frame)
        self.first_name_entry.grid(row=5, columnspan=1, sticky="e")
        
        # address
        address_label = Label(add_frame, text="2. Address:", fg="#152238", bg="white", font=child_window_label_font)
        address_label.grid(row=6, column=0, pady=3, padx=1, sticky="w")
        self.address_entry = Text(add_frame, width=48, height=2,font=("Montserrat", 11) )
        self.address_entry.grid(row=7, column=0, sticky="w")
        
        # Contact Number
        contact_number_label = Label(add_frame, text="3. Contact Number:", fg="#152238", bg="white", font=child_window_label_font)
        contact_number_label.grid(row=9, column=0, pady=3, padx= 1, sticky="w")
        self.contact_number_entry = Entry(add_frame)
        self.contact_number_entry.grid(row=9, columnspan=1, sticky="e")
        
        # email
        email_label = Label(add_frame, text="4. Email Address:", fg="#152238", bg="white", font=child_window_label_font)
        email_label.grid(row=10, column=0, pady=3, padx= 1, sticky="w")
        self.email_entry = Entry(add_frame)
        self.email_entry.grid(row=10, columnspan=1, sticky="e")
        
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
        contact_person_details = Label(add_frame, text="Contact Person Details", fg="#007fff", bg="white", height=1, font=child_window_label_font)
        contact_person_details.grid(row=16, columnspan=1, sticky="w", pady=3, padx=3) 

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
    
        # Create a button that will add the new record
        add_record = Button(add_frame, text="Add Record", width=10, height=1, fg="#003a88", bg="#90b1db", relief=GROOVE, font=child_window_label_font, justify="right", command=self.data_privacy)
        add_record.grid(row=19, columnspan=1, padx=10, pady=10, sticky="e")

        # Center the window on the screen.
        add_window.update_idletasks()
        screen_width = add_window.winfo_screenwidth()
        screen_height = add_window.winfo_screenheight()
        x = (screen_width - add_window.winfo_width()) // 2
        y = (screen_height - add_window.winfo_height()) // 2
        add_window.geometry('+{}+{}'.format(x, y))

    # Def function for data privacy agreement
    def data_privacy(self):
        # Data Privacy Window
        self.data_privacy_window = Toplevel(self.main)
        self.data_privacy_window.title("Data Privacy")
        self.data_privacy_window.geometry("300x300")
        self.data_privacy_window.configure(bg="white")
        # Var for data privacy message
        data_privacy_text = """I hereby authorize the application to collect and process the data listed here so that the COVID-19 infection can be controlled. I am aware that the Data Privacy Act of 2012 protects my personal information. If needed, this information may be used to help Medical Services and/or LGU find my contact information. I also know that the RA 11469 Bayanihan to Heal as One Act requires me to give accurate information. Click the OK Button to proceed. Otherwise, click the cancel button."""
        # label widget
        data_privacy_label = Label(self.data_privacy_window, text=data_privacy_text, bg="white", fg="black", font=("Oxygen Bold", 11), wraplength=280, justify="left")
        data_privacy_label.pack(padx=10, pady=10)
        # button widget for ok
        data_privacy_ok_button = Button(self.data_privacy_window, text="OK", width=10, height=1, fg="#003a88", bg="#90b1db", relief=GROOVE, font=("Montserrat", 13, "bold"), command=self.close_data_privacy_and_add_record)
        data_privacy_ok_button.pack(padx=10, pady=10, side=RIGHT)
        # button widgets for cancel
        data_privacy_cancel_button = Button(self.data_privacy_window, text="Cancel", width=10, height=1, fg="#003a88", bg="#90b1db", relief=GROOVE, font=("Montserrat", 13, "bold"), command=self.data_privacy_window.destroy)
        data_privacy_cancel_button.pack(padx=10, pady=10, side=LEFT)
        # Make the Label widget non-editable
        data_privacy_label.config(state="disabled")
        
        # Center the window on the screen.
        self.data_privacy_window.update_idletasks()
        screen_width = self.data_privacy_window.winfo_screenwidth()
        screen_height = self.data_privacy_window.winfo_screenheight()
        x = (screen_width - self.data_privacy_window.winfo_width()) // 2
        y = (screen_height - self.data_privacy_window.winfo_height()) // 2
        self.data_privacy_window.geometry('+{}+{}'.format(x, y))
    
    # def function that will close the data privacy window when you click ok
    def close_data_privacy_and_add_record(self):
        if self.data_privacy_window:
            self.data_privacy_window.destroy()
            self.add_record_action()

    # Def function that will to get the data entered
    def add_record_action(self):
        last_name = self.last_name_entry.get()
        first_name = self.first_name_entry.get()
        address = self.address_entry.get("1.0", END).strip()
        contact_number = self.contact_number_entry.get()
        email = self.email_entry.get()
        vaccine = self.vaccine_var.get()
        contact_person_name = self.contact_person_name_label_entry.get()
        contact_person_phone = self.contact_person_phone_entry.get()

        # Check if the entered data fills the needed data.
        fields = [
            ("Last Name", last_name),
            ("First Name", first_name),
            ("Address", address),
            ("Contact Number", contact_number),
            ("Email", email),
            ("Vaccine", vaccine),
            ("Contact Person's Name", contact_person_name),
            ("Contact Person's Phone", contact_person_phone)
            ]
        # Check if any required information is empty
        for field_name, field_value in fields:
            if not field_value:
                messagebox.showerror("Error", f"Please fill in the required field: {field_name}")
                return False
            
        # Check if the numbers are all int for 
        # contact_number
        try:
            contact_number_int = int(contact_number)
            if len(contact_number) != 11:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Your Contact number must be a valid 11-digit number.")
            return
        # contact_person_phone
        try:
            contact_person_phone_int = int(contact_person_phone)
            if len(contact_person_phone) != 11:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Contact person's phone number must be a valid 11-digit number.")
            return 
        
        # Create an instance of ContactTracingRecords
        name = f"{last_name}, {first_name}"
        entry = ContactTracingRecords(last_name, first_name, address, contact_number, email, vaccine, contact_person_name, contact_person_phone)
        try:
            # Save the records to a file
            self.contact_tracing_app.add_records(entry)
            self.contact_tracing_app.save_records("contact_tracing_records.txt")
            messagebox.showinfo("Success", "Record added and saved successfully.")
            if self.data_privacy_window:
                self.data_privacy_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the record: {e}")
            return 
        
    # Define function that will search the user's information
    def search_record(self):
        # Create a child window
        search_window = Toplevel(self.main)
        search_window.title("Search Record")
        search_window.geometry("1300x400")
        search_window.configure(bg="white")

        # Create a label and entry field for the user to enter the name they want to search for
        search_label = Label(search_window, text="Enter Name to Search:", fg="#152238", bg="white", font=("Montserrat", 12, "bold"))
        search_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # Create a StringVar to hold the search query
        search_info_var = StringVar()

        search_entry = Entry(search_window, font=("Montserrat", 12), width=90, textvariable=search_info_var)
        search_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        # Create a button to initiate the search
        search_button = Button(
            search_window,
            text="Search",
            width=20,
            height=1,
            fg="#003a88",
            bg="#90b1db",
            relief=GROOVE,
            font=("Montserrat", 12, "bold"),
            command=lambda: self.search_record_action(search_entry.get())
            )
        search_button.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        # Create a frame to display the search results
        results_frame = Frame(search_window, bg="#white", width=100, height= 325)
        results_frame.grid(row=1, column=0, columnspan=3, pady=10, padx=5)
        self.results_frame = results_frame

        # Center the window on the screen.
        search_window.update_idletasks()
        screen_width = search_window.winfo_screenwidth()
        screen_height = search_window.winfo_screenheight()
        x = (screen_width - search_window.winfo_width()) // 2
        y = (screen_height - search_window.winfo_height()) // 2
        search_window.geometry('+{}+{}'.format(x, y))

    # Define the search action
    def search_record_action(self, search_query):
        self.contact_tracing_app.read_records("contact_tracing_records.txt")

        # Check if the input is valid
        if not search_query.strip():
            messagebox.showerror("Error", "Please enter a valid search query.")
            return

        # Search for matching entries
        self.match_entry = self.contact_tracing_app.search_records(search_key=search_query)

        # Display the search results
        self.display_search_results()

    # Define display search results
    def display_search_results(self):
        # Clear any previous search results from the frame
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Display the search results
        if self.match_entry:
            self.create_result_frame()
        else:
            no_result_label = Label(self.results_frame, text="No matching records found.", fg="#152238", bg="white", font=("Montserrat", 11, "italic"))
            no_result_label.pack(anchor="w")

    # Create a method to create and populate the result frame
    def create_result_frame(self):
        # Create a Treeview widget
        self.results_treeview = ttk.Treeview(self.results_frame)

        # Define the columns and their headings
        self.results_treeview["columns"] = ("Name", "Address", "Contact Number", "Email Address", "Vaccine Status", "Contact Person Name", "Contact Person Phone Number")
        self.results_treeview.heading("#0", text="Record")
        self.results_treeview.heading("Name", text="Name")
        self.results_treeview.heading("Address", text="Address")
        self.results_treeview.heading("Contact Number", text="Contact Number")
        self.results_treeview.heading("Email Address", text="Email Address")
        self.results_treeview.heading("Vaccine Status", text="Vaccine Status")
        self.results_treeview.heading("Contact Person Name", text="Contact Person Name")
        self.results_treeview.heading("Contact Person Phone Number", text="Contact Person Phone Number")

        # Set the column widths
        self.results_treeview.column("#0", width=80)
        self.results_treeview.column("Name", width=150)
        self.results_treeview.column("Address", width=200)
        self.results_treeview.column("Contact Number", width=150)
        self.results_treeview.column("Email Address", width=200)
        self.results_treeview.column("Vaccine Status", width=150)
        self.results_treeview.column("Contact Person Name", width=150)
        self.results_treeview.column("Contact Person Phone Number", width=180)

        # Insert the search results into the Treeview
        for idx, entry in enumerate(self.match_entry):
            record_number = f"Record {idx + 1}"
            self.results_treeview.insert("", "end", text=record_number, values=(entry.name, entry.address, entry.contact_number, entry.email, entry.vaccine, entry.contact_person_name, entry.contact_person_phone))

        # Attach a scrollbar to the Treeview
        scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.results_treeview.yview)
        self.results_treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the Treeview
        self.results_treeview.pack(fill="both", expand=True)
