# Programmed by: Rebekah Joy E. Sevial
# Program to store the records for contact tracing

# Create a class that stores the information of the person who answered the app
class ContactTracingRecords:
    def __init__(self, last_name, first_name, address, contact_number, email, vaccine, contact_person_name, contact_person_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.contact_number = contact_number
        self.email = email
        self.vaccine = vaccine
        self.contact_person_name = contact_person_name
        self.contact_person_phone = contact_person_phone
        self.name = f"{last_name}, {first_name}"