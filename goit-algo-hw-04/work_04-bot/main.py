from colorama import init, Fore
from handlers import parse_input, add_contact, change_contact, show_phone, show_all

init(autoreset=True)

bot_comamand_list = """
Commands:
hello - greeting
add [name] [phone number] - adding a username with a phone numbe
change [name] [phone number] - changing contact phone number by name
phone [name] - search for phone number by contact name
all - show all contact list
close, exit - bot shutdown
"""


def main():
    contacts = {}
    print(Fore.BLUE + "Welcome to the assistant bot!")
    print(f"{Fore.YELLOW} {bot_comamand_list}")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["exit", "close"]:
            print(f"{Fore.BLUE}Goodbye!")
            break
        elif command == "hello":
            print(f"{Fore.BLUE}How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))  
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(f"{Fore.RED}Invalid command.")



if __name__ == "__main__":
    main()

