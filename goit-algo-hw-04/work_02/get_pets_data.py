
def read_file(path: str) -> list[str]:
    try:
        with open(path, encoding='utf-8') as file:
            pets = file.readlines()
            return pets
    except FileNotFoundError:
        print(f"File {path} not found")
    except Exception as e:
        print(e)
        
def convert_pets_data(pets_data: list[str]) -> list[dict]:
    pet_list = []
    
    for pet in pets_data:
        id, name, age = pet.strip().split(',')
        pet_list.append({"id": id, "name": name, "age": age})
        
    return pet_list

def get_cats_info(path: str) -> list[dict]:
    pet_list = read_file(path)
    return convert_pets_data(pet_list) 