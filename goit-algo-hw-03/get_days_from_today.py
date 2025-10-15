from datetime import datetime
from typing import Optional


# calculating the difference in days between the current date and the next date
def get_days_from_today(some_date:str)-> Optional[int]:
    """
    The function takes one parameter: date — a string representing a date in the format 'YYYY-MM-DD'.
    The function returns an integer indicating the number of days from the given date to the current one. 
    If the given date is later than the current one, the result must be negative.
    """

    try:
       income_date = datetime.strptime(some_date, '%Y-%m-%d').date() # converting a date string to an object datetime
    except ValueError as e:
        raise ValueError("Incorrect date format. Use YYYY-MM-DD.") from e
    else:
        current_day = datetime.today().date() # getting the current date
        difference = income_date - current_day     
        return difference.days    

    

  
# print(get_days_from_today('2025-02-25'))
# print(get_days_from_today('2025.02.25'))
# print(get_days_from_today('2025-11-11'))

