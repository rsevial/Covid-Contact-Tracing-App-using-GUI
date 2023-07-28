# Programmed by: Rebekah Joy E. Sevial
# Contact Tracing Application (Add and Search Entry)

# Import the class from other files that store the info of the user
from records import ContactTracingRecords

# Create a class named ContactTracingApp that will perform
class ContactTracingApp:
    def __init__(self, filename):
        self.entries = []
        self.read_records(filename) 
    # Def function for add entry
    def add_records(self, records):
        self.entries.append(records)
    # Def function to write and save the file
    def save_records(self, filename):
        with open(filename, 'w') as file:
            for entry in self.entries:
                name = f"{entry.last_name}, {entry.first_name}"  # Reconstruct the name from last_name and first_name
                file.write(f"{name}, {entry.address}, {entry.contact_number}, {entry.email}, {entry.vaccine}, {entry.contact_person_name}, {entry.contact_person_phone}\n")  
    # Def function that will load and read the file
    def read_records(self, filename):
        self.entries.clear()
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 8:  # Updated to match the number of fields in the record
                    last_name, first_name, address, contact_number, email, vaccine, contact_person_name, contact_person_phone = data
                    entry = ContactTracingRecords(last_name, first_name, address, contact_number, email, vaccine, contact_person_name, contact_person_phone)
                    self.add_records(entry)
    # Def function for search entry
    def search_records(self, search_key):
        match_entry = []
        search_key = search_key.lower().strip()  # Convert the search key to lowercase and remove leading/trailing spaces
        for entry in self.entries:
            if search_key in entry.name.lower():  # Check if the search key is present in the lowercased name
                match_entry.append(entry)
        return match_entry