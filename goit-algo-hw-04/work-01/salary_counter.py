


def get_workers_data(path: str) -> list[str]:
    """
    The function opens a file at the passed path, reads data from it, and returns a list of lines from the file
    ["Alex Korp,3000", "Nikita Borisenko,2000"]
    Handles exceptions if there are errors while opening or reading data.
    """
    try:
        with open(path, encoding='utf-8') as file:
            workers = file.readlines()
            return workers
    except FileNotFoundError:
        print(f"File {path} not found")
    except Exception as e:
        print(e)
    

def get_salary_data(employee_list: list[str]) -> tuple:
    """
    The function receives a list ["Alex Korp,3000", "Nikita Borisenko,2000"] 
    and returns a new list of salary amounts ["3000", "2000"]
    """
    salary_list = []

    for employee in employee_list:
        _, salary = employee.split(',')
        salary_list.append(salary.strip()) 
    
    return salary_list



def total_salary(path: str) -> tuple | list:
    """
    Calculation of the total salaries amount and the average salary of employees.

    The function receives a path to a .txt file that contains data in the following format:
    Alex Korp,3000
    Nikita Borisenko,2000
    Sitarama Raju,1000

    and returns a tuple (total amount, average salary)
    """
    
    employee_list = get_workers_data(path)
    salary_list =  get_salary_data(employee_list)
   
    total_amount = 0
              
    for item in salary_list:
        total_amount += float(item)

    return (total_amount, total_amount / len(salary_list))