# Programmed by: Rebekah Joy E. Sevial
# Contact Tracing Application (Add and Search Entry)

# Import the class from other files that store the info of the user
from records import ContactTracingRecords

# Create a class named ContactTracingApp that will perform
class ContactTracingApp:
    def __init__(self):
        # create varible that will store the info of the user in a list
        self.entries = []
    # Def function for add entry
    def add_record(self, records):
        self.entries.append(records)
    # Def function to write and save the file
    def save_records(self, filename):
       with open(filename, 'w') as file:
            for entry in self.save_records:
                file.write(f"{entry.name}, {entry.address}, {entry.contact_number}, {entry.email}, {entry.vaccine}, {entry.vaccine_result}, {entry.contact_person_name}, {entry.contact_person_phone}\n")
 
    # Def function that will load and read the file
    # Def function for search entry