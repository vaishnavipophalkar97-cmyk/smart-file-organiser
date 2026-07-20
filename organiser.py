import shutil
from pathlib import Path

def get_file_path(): 
    folder = input("Enter the path of the folder you want to organize: ")
    path = Path(folder)
    EXTENSION_MAP= {
        ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".mp3": "Audio",
    ".zip": "Archives"
    }
    
    if path.exists():
        for file in path.iterdir():
            if file.is_dir():
                continue  # Skip directories
            ext = file.suffix.lower()
            folder_name = EXTENSION_MAP.get(ext, "Others")  # Default folder for unknown extensions
            #Defining target folder path
            target_folder = path / folder_name
            
            #Create folder if it is not already there
            target_folder.mkdir(exist_ok=True)

            #Define file's new destination path
            dest = target_folder / file.name

            #Move the file!
            shutil.move(str(file), str(dest))
            
            print(f"Moved {file.name} to {target_folder}")
    else:
        print("Error finding : Directory does not exist.")

get_file_path()
