class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print("--------------------")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                results.append(contact)
        if results:
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print("--------------------")
        else:
            print("No contacts found matching your query.")

    def update_contact(self, name, new_details):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_details['phone_number']
                contact.email = new_details['email']
                contact.address = new_details['address']
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

# Example usage:
contact_book = ContactBook()

# Add contacts
contact_book.add_contact(Contact("Bunny", "123-456-7890", "bunny@example.com", "123 Main St"))
contact_book.add_contact(Contact("Gopi", "987-654-3210", "gopi@example.com", "456 Elm St"))

# View contacts
contact_book.view_contacts()

# Search contacts
contact_book.search_contact("Bunny")

# Update contact
new_details = {'phone_number': '555-555-5555', 'email': 'Bunny_new@example.com', 'address': '789 Oak St'}
contact_book.update_contact("Bunny", new_details)

# Delete contact
contact_book.delete_contact("Gopi")