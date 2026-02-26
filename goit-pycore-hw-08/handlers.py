from colorama import  Fore
from typing import Callable
from datetime import datetime
from _classes import AddressBook, Record



def parse_input(user_input:str):
    """Parses the input into a command and list of arguments."""
    if not user_input.strip():
        return "_"
    
    command, *args = user_input.split()
    command = command.strip().lower()
    
    return command, *args

def input_error(func) -> Callable:
    """
    Returns the handler-function or returns an error message.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{Fore.RED}Enter name and phone please."
        except KeyError:
            return f"{Fore.RED}Such contact does not exist."
        except IndexError:
            return f"{Fore.RED}Enter user name please."
        except AttributeError:
            return f"{Fore.RED}This entry is missing."
        except Exception as e:
            return(f"{Fore.RED}{e}")
    return inner

@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    """Adds a contact to the dict (name and phone number)."""
    name, phone_number, *_ = args
    record = book.find(name)
    message = f"{Fore.GREEN}Contact updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"{Fore.GREEN}Contact added."
    if phone_number:
        record.add_phone(phone_number)
    return message
    
@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    """Updates an existing contact's phone."""
    name, old_phone_number, new_phone_number, *_ = args
    record:Record = book.find(name)
               
    record.edit_phone(old_phone_number, new_phone_number)    
    return f"{Fore.GREEN}Contact updated."
   
            
@input_error   
def show_phone(args: list[str], book: AddressBook) -> str:
    """Returns a phone number by name."""
    name = args[0].strip().lower()
    record:Record = book.find(name)
              
    phones = "; ".join(p.value for p in record.phones)
    return f"{Fore.GREEN}{phones}"
      
    
@input_error
def show_all(book: AddressBook) -> str:
    """Returns all contacts as lines."""
    if not book:
        raise Exception("No contacts yet.")

    return f"{Fore.GREEN}{str(book)}"

@input_error
def add_birthday(args:list[str], book:AddressBook) -> str:
    """Add date of birth for the specified contact in the format DD.MM.YYYY"""
    try:
        name, birthday, *_ = args
    except ValueError:
         raise Exception("Please enter name and date of birth.")
    
    record:Record = book.find(name)
       
        
    if record.birthday:
        message = "Birthday updated."
    else:
        message = 'Birthday added.'
       
    record.add_birthday(birthday)    
    return f"{Fore.GREEN}{message}"

@input_error
def show_birthday(args:list[str], book:AddressBook) -> str:
    """Returns a date of birth by name."""
    try:
        name, *_ = args
    except ValueError:
         raise Exception("Please enter name.")
    
    record:Record = book.find(name)
      
    birthday = record.birthday.value
    if birthday is None:
        return f"{Fore.RED}The contact does not have a date of birth set."
    return f"{Fore.GREEN}{birthday}"

@input_error
def birthdays(book:AddressBook) -> str:
    """Returns a list of users to be greeted by day of the week next week"""
    result = book.get_upcoming_birthdays()
    if not result:
        return f"{Fore.RED}No birthdays in the next 7 days."
    lines = [f"Name: {item['name']}, birthday: {item['birthday']}" for item in result]
    return f"{Fore.GREEN}" + "\n".join(lines)
