from colorama import  Fore
from typing import Callable


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
        except Exception as e:
            return(f"{Fore.RED}{e}")
    return inner

@input_error
def add_contact(args: list[str], contacts: dict) -> str:
    """Adds a contact to the dict."""
    name, phone_number = args
    
    if name in contacts:
        raise Exception(f"{Fore.MAGENTA}A contact with that name already exists. Please enter a different name.")
    
    contacts[name.strip()] = phone_number.strip()
    return f"{Fore.GREEN}Contact added."

@input_error
def change_contact(args: list[str], contacts: dict) -> str:
    """Updates an existing contact's phone."""
    name, phone_number = args
    
    contact = contacts[name.strip()]  #To handle KeyError in a decorator
    contacts[name.strip()] = phone_number.strip()
        
    return f"{Fore.GREEN}Contact updated."
   
            
@input_error   
def show_phone(args: list[str], contacts: dict) -> str:
    """Returns a phone number by name."""
    name = args[0].strip().lower()
    
    contact = contacts[name] #To handle KeyError in a decorator
    return f"{Fore.GREEN}{contact}"
   
    
@input_error
def show_all(contacts: dict) -> str:
    """Returns all contacts as lines."""
    if not contacts:
        raise Exception("No contacts yet.")
       

    lines = [f"{Fore.GREEN}{key}: {value}" for key, value in contacts.items()]
    return "\n".join(lines)