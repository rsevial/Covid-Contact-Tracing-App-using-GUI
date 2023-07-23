# Programmed by: Rebekah Joy E. Sevial
# Program to store the records for contact tracing

# Create a class that stores the information of the person who answered the app
class ContactTracingRecords:
    def __init__(self, name, address, contact_number, vaccine, vaccine_result, contact_person_name, contact_person_phone, date_visited):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.vaccine = vaccine
        self.vaccine_result = vaccine_result
        self.contact_person_name = contact_person_name
        self.contact_person_phone = contact_person_phone
        self.date_visited = date_visited


