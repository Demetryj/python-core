from pathlib import Path
from get_pets_data import get_cats_info




def main():
    base_path = Path(__file__).resolve().parent
    file_path = base_path / "pets.txt"
    
    cats_info = get_cats_info(file_path)
    print(cats_info)
   

if __name__ == "__main__":
    main()