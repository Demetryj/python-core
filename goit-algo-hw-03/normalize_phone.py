import re

raw_numbers = [
    "067\\t123 4567",
    "(095)+ 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "8050-343-25-52"
]

# phone number normalization function
def normalize_phone(phone_number :str)->str:
    """
    1. The phone_number function parameter is a string with a phone number in various formats.
    2. The function removes all characters except digits and the '+' character.
    3. If the international code is missing, the function adds the code '+38'. 
    4. This takes into account cases where the number starts with '380' (only '+' is added) and when the number starts without a code ('+38' is added).
    The function returns the normalized phone number as a string (+380XXXXXXXXX).
    """

    trim_number = phone_number.strip() # remove spaces if any

# remove all characters except numbers and + if it is at the beginning of the number
    formated_number = re.sub(r'(?!^)\+|[^\d+]', '', trim_number) 

    if formated_number.startswith('+380'):
        return formated_number
    
    if formated_number.startswith('380'):
        return "+" + formated_number

    if formated_number.startswith('8'):
        return "+3" + formated_number
    
    if formated_number.startswith('0'):
        return "+38" + formated_number
    
  
    
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Normalized phone numbers for SMS sending:", sanitized_numbers)