from pathlib import Path
from salary_counter import total_salary


# print(Path.cwd())

def main():
    base_path = Path(__file__).resolve().parent
    file_path = base_path / "workers.txt" 
      
    total, average = total_salary(file_path)
    print(f"Total salary: {total}, Average salary: {average}")


if __name__ == "__main__":
    main()