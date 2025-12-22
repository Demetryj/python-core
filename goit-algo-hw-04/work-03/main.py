"""Prints a directory tree with colored formatting."""
from colorama import init, Fore
import sys
from pathlib import Path

init(autoreset=True)


def pars_folders_and_files_by_path(path: Path, indent: int = 0):
    """Recursively prints folder contents with indentation."""
    if indent == 0:
        print(f"{Fore.BLUE}{path.name}/")

    # Iterate through directory items and print with indentation.
    for item in path.iterdir():
        prefix = "  |" * (indent + 1)
        if item.is_dir():
            print(f"{prefix}──{Fore.BLUE}{item.name}/")
            pars_folders_and_files_by_path(item, indent + 1)
        elif item.is_file():
            print(f"{prefix}--{Fore.YELLOW}{item.name}")
    

def main():
    try:
        # Read path from command-line arguments.
        path_arg = sys.argv[1]
        path = Path(path_arg)
        
        # Expand user home and resolve to an absolute path.
        path = Path(path_arg).expanduser().resolve()
        

        # Ensure the path exists and is a directory.
        if not path.exists() or not path.is_dir():
            raise ValueError("Invalid directory path.")

        pars_folders_and_files_by_path(path)
        
        
    except IndexError:
        print(f"{Fore.RED}No directory path specified")
    except Exception as e:
        print(f"{Fore.RED}{e}")
   
    



if __name__ == "__main__":    
    main()    
