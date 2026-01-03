"""
Скрипт, який читає лог-файл, переданий як аргумент командного рядка,
і виводить статистику за рівнями логування наприклад, INFO, ERROR, DEBUG, WARNING. 
Також, якщо користувач вкаже рівень логування, як другий аргумент командного рядка, 
виводить всі записи цього рівня.
"""

import sys
from pathlib import Path
from colorama import init, Fore
from  collections import Counter

init(autoreset=True)

def parse_log_line(line: str) -> dict:
    """
    Функція виконує парсинг рядка логу.
    Функція приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення
    {
        "date_time": "2024-01-22 09:00:45",
        "log_level": "INFO" | "DEBUG" | "ERROR" | "WARNING",
        "log": "log message"
    }
    """
    date, time, log_level, *log = line.split()
    return {
        "date_time": f"{date} {time}",
        "log_level": log_level,
        "log": " ".join(log)
        }
    
    
def load_logs(file_path: str) -> list:
    """
    Функція виконує завантаження лог-файлів.
    Повертає список словників з даними логів: дата, рівень логування, запис логу:
    [{
        "date_time": "2024-01-22 09:00:45",
        "log_level": "INFO" | "DEBUG" | "ERROR" | "WARNING",
        "log": "log message"
    }]
    """
    
    try:
        with open(file_path, encoding='utf-8') as fh:
            return ([parse_log_line(log_line ) for log_line in fh])
               
    except PermissionError:
        print(f"{Fore.RED}Немає прав на читання: {file_path}")
    except OSError as e:
        print(f"{Fore.RED}Помилка читання файлу {file_path}: {e}")
    

def count_logs_by_level(logs: list) -> dict:
    """
    Функція робить підрахунок записів за кожним рівнем логування.
    Повертає словник із кількістю записів для кожного рівня логування.
    {
        "INFO": 5,
        "DEBUG": 0,
        "ERROR": 1,
        "WARNING": 2
    }
    """
    counts = Counter(item.get("log_level") for item in logs)
    return dict(counts)

    
def display_log_counts(counts: dict):
    """
    Виведення результатів: кількість записів для кожного рівня логування та
    детальна інформація для рівня логування у разі його вкузування у другим аргументом командного рядка.
    Функція отримує словник типу 
    {
        "INFO": 5,
        "DEBUG": 0,
        "ERROR": 1,
        "WARNING": 2
    }
    """
    
    header = "Рівень логування | Кількість"
    separetor = "-" * 17 + "|" + "-" * 10
    print(f"\n{header}")
    print(separetor)
    for log_level, quantity in counts.items():
        print(f"{log_level:<16} | {quantity}")
        

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Функція виконує фільтрацію списку словників логів за рівнем логування.
    Повертає список логів вказаного у командному рядку рівня логування.
    """
    
    level = level.upper()
    return list(filter(lambda item: item.get("log_level") == level, logs))

def display_log_level_details(feltered_logs_by_level: list, log: str):
    """ 
    Функція отримує у якості аргументів відфільтрований за рівнем логування список типу: 
    [{
        "date_time": "2024-01-22 09:00:45",
        "log_level": "INFO" | "DEBUG" | "ERROR" | "WARNING",
        "log": "log message"
    }]
    та рівнем логування.
    Виводить в термінал інформацію, стосовно рівня логування.
    """
    
    if not feltered_logs_by_level:
        print(f"\n{Fore.RED}Рівень логування '{log.upper()}' відсутній.")
        return
    
    header = f"\nДеталі логів для рівня '{log.upper()}':"
    print(header)
    for item in feltered_logs_by_level:
        print(f"{item["date_time"]} - {item["log"]}")

def main():
    try:
        path_args = sys.argv
        log_file_path = Path(path_args[1]).expanduser().resolve()
        
        if not log_file_path.exists():
            raise Exception(f"{Fore.RED}Файл не знайдено: {log_file_path}")
        if not log_file_path.is_file():
            raise Exception(f"{Fore.RED}Це не файл: {log_file_path}")
        
        logs = load_logs(log_file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        
        # Якщо вказано другий аргумент в командному рядку (рівень логування)
        # виводимо детальну фінформацію по зазначеному рівню логування
        if len(path_args) >= 3: 
            log_level = path_args[2]
            filtered_log_list = filter_logs_by_level(logs, log_level)
            display_log_level_details(filtered_log_list, log_level)
            
    except IndexError:
        print(f"{Fore.RED}Шлях до файлу логів не вказано")
    except Exception as e:
        print(f"{Fore.RED}{e}")

if __name__ == "__main__":
    main()