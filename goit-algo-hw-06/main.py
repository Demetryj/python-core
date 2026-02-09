from collections import UserDict 

class FormatPhoneNumber(Exception):
    pass

class Field:
    """Base class for record fields."""
    
    def __init__(self, value:str):
        self.value = value
    
    def __str__(self):
        return str(self.value)

class Name(Field):
    """Class for storing a contact name. Required field."""
    pass

class Phone(Field):
    """Class for storing a phone number. Validates format (10 digits)."""
    def __init__(self, value):
        super().__init__(value)
        if len(value) !=10:
            raise FormatPhoneNumber("Phone number must consist of 10 digits")
        for char in value:
            if not char.isdigit():
                raise FormatPhoneNumber("The phone number must contain only numbers.")
                
    
class Record:
    """
    Class for storing contact info, including a name and a list of phone numbers.
    Add phone numbers.
    Remove phone numbers.
    Edit phone numbers.
    Search for a phone number.
    """
    def __init__(self, name:str):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone_number:str):
        self.phones.append(Phone(phone_number))
        
    def remove_phone(self, phone_number:str):
        phone = self.find_phone(phone_number)
        if not phone:
            raise ValueError("Phone number not found.")
        self.phones.remove(phone)
        
    def edit_phone(self, old_phone_number, new_phone_number):
        phone = self.find_phone(old_phone_number)
        if not phone:
            raise ValueError("Phone number not found.")
        self.phones[self.phones.index(phone)] = Phone(new_phone_number)
        
    def find_phone(self, phone_number:str):
        return next((phone for phone in self.phones if phone.value == phone_number), None)
    
    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    """
    Class for storing and managing records.
    Add records.
    Find records by name.
    Delete records by name.
    Record: add phone numbers.
    """
    def add_record(self, new_record):
        self.data[new_record.name.value] = new_record
        
    def find(self, contact_name:str):
        return self.data.get(contact_name)
            
    def delete(self, contact_name:str):
        contact = self.data.get(contact_name)
        if contact:
            self.data.pop(contact_name)
            
    def __str__(self):
        lines = []
        for record in self.data.values():
            lines.append(str(record))
        return "\n".join(lines)


if __name__ == "__main__":
    book = AddressBook()
   
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    
    book.add_record(john_record)
    
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    
    book.add_record(jane_record)
    
    print(book)
    
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    
    print(john)  

   
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  

   
    book.delete("Jane")