from colorama import init, Fore

from handlers import (
    parse_input, 
    add_contact, 
    change_contact,
    show_phone, 
    show_all,
    add_birthday,
    show_birthday,
    birthdays
)
from save_data_func import load_data, save_data

init(autoreset=True)


bot_comamand_list = """
Commands:
hello - greeting
add [name] [phone number] - adding a username with a phone numbe
change [name] [old phone number] [new phone number]- changing contact phone number by name
phone [name] - search for phone number by contact name
add-birthday [name] [birthday] - add date of birth for the specified contact in the format DD.MM.YYYY
show-birthday [name] - show date of birth for the specified contact
birthdays - show birthdays for the next 7 days with dates when they should be celebrated
all - show all contact list
close, exit - bot shutdown
"""


def main():
    book = load_data()
    print(Fore.BLUE + "Welcome to the assistant bot!")
    print(f"{Fore.YELLOW} {bot_comamand_list}")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["exit", "close"]:
            save_data(book)
            print(f"{Fore.BLUE}Goodbye!")
            break
        elif command == "hello":
            print(f"{Fore.BLUE}How can I help you?")
        elif command == "add":
            print(add_contact(args, book))  
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print(f"{Fore.RED}Invalid command.")

if __name__ == "__main__":
    main()
  