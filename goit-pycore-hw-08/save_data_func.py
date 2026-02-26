from pickle import dump, load

from _classes import AddressBook

def save_data(book: AddressBook, filename:str = "addressbook.pkl") -> None:
    """Serialization of the contacts object (contact book)"""
    with open(filename, 'wb') as fh:
        dump(book, fh)
        
def load_data(filename:str = "addressbook.pkl") -> AddressBook:
    """Deserialization of the contacts object (contact book)"""
    try:
        with open(filename, "rb") as fh:
            return load(fh)
    except FileNotFoundError:
        return AddressBook()