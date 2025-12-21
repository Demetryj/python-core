from colorama import  Fore

def parse_input(user_input):
    """Parses the input into a command and list of arguments."""
    command, *args = user_input.split()
    command = command.strip().lower()
    
    return command, *args

def unpack_name_phone(args: list[str]) -> tuple[str, str] | str:
    """Returns (name, phone) or a format error message."""
    try:
        name, phone_number = args
        return name.strip().lower(), phone_number.strip().lower()
    except ValueError:
        return f"{Fore.RED}There must be two arguments after the command: [name] [phone number]"


def validation_args(name:str, phone_number:str) -> str:
    """Validates name and phone number; returns an error message if invalid."""
    # if not name.isalpha():
    #     return(f"{Fore.RED}The first argument must be a name.")
    
    if not phone_number.isdigit():
        return(f"{Fore.RED}The second argument must be a phone number.")

def add_contact(args: list[str], contacts: dict) -> str:
    """Adds a contact to the dict or returns an error message."""
    result = unpack_name_phone(args)
    if isinstance(result, str):
        return result
    name, phone_number = result
    
    has_contact = contacts.get(name)
    if has_contact:
        return(f"{Fore.MAGENTA}A contact with that name already exists. Please enter a different name.")
    
    error_message = validation_args(name, phone_number)
    if error_message:
        return error_message
    
    contacts[name.strip()] = phone_number.strip()
    return f"{Fore.GREEN}Contact added."

def change_contact(args: list[str], contacts: dict) -> str:
    """Updates an existing contact's phone or returns an error message."""
    result = unpack_name_phone(args)
    if isinstance(result, str):
        return result
    name, phone_number = result
    
    error_message = validation_args(name, phone_number)
    if error_message:
        return error_message
    
    has_contact = contacts.get(name)
    if has_contact:
        contacts[name] = phone_number
        return f"{Fore.GREEN}Contact updated."
    else:
        return f"{Fore.RED}A contact with name {name} does not exist."    
    
def show_phone(args: list[str], contacts: dict) -> str:
    """Returns a phone number by name or an error message."""
    try:
        name = args[0].strip().lower()
    except IndexError:
         return f"{Fore.RED}The contact name must be specified after the command."
        
    contact = contacts.get(name)
    if contact:
        return f"{Fore.GREEN}{contact}"
    else:
        return f"{Fore.RED}A contact with name {name} does not exist."
    

def show_all(contacts: dict) -> str:
    """Returns all contacts as lines or a message for an empty list."""
    if not contacts:
        return f"{Fore.MAGENTA}No contacts yet."  

    lines = [f"{Fore.GREEN}{key}: {value}" for key, value in contacts.items()]
    return "\n".join(lines)