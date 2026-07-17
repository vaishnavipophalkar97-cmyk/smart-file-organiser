# smart-file-organiser
A solution made to smartly organize your folder
## 📁 Smart File Organizer

A lightweight, cross-platform Python utility designed to automate desktop clutter management. This script scans a designated target directory, detects file types based on their extensions, and dynamically moves them into structured subfolders (e.g., Documents, Images, Audio).

Built entirely using modern standard libraries, this project is designed to be safe, reliable, and completely customizable.

## 🛠️ How It Works

This organizer follows a structured 4-step pipeline:

Targeting: Dynamically resolves your computer's Desktop path using cross-platform libraries (supports Windows, macOS, and Linux).

Scanning: Iterates through all items within a designated target folder, ignoring existing folders and subdirectories.

Classification: Detects the lowercase suffix (extension) of each file and checks it against a mapped dictionary of rules.

Filing: Safely creates target directories (if they do not already exist) and relocates files using safe system moves.

## 🚀 Getting Started

1. Prerequisites

You need Python 3.6+ installed on your machine. You can verify your installation by running:

python --version


2. Installation & Setup

Clone this repository (or download the source files) to your local machine:

git clone https://github.com/vaishnavipophalkar97-cmyk/smart-file-organizer.git
cd smart-file-organizer


3. Running the Script

By default, the script is configured to look for a folder named organizer_sandbox on your Desktop.

Create a folder named organizer_sandbox on your Desktop.

Put some test files inside (e.g., test.pdf, photo.jpg, song.mp3).

Run the organizer:

python organizer.py


## ⚙️ Customization (How to change the rules)

You can easily customize where your files go by editing the EXTENSION_MAP dictionary inside organizer.py:

EXTENSION_MAP = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".mp3": "Audio",
    ".zip": "Archives"
}


To add a new rule (e.g., routing .xlsx files to a "Spreadsheets" folder), simply add a new key-value pair to the dictionary:

    ".xlsx": "Spreadsheets",



## 🎯 Next-Level Goals (In Progress)

Here are the features I am planning to implement next to make this tool even more robust:

[ ] The "Others" Catch-All: Automatically route unrecognized file extensions to a Misc/ folder instead of skipping them.

[ ] Duplicate Prevention: Add logical checks to rename incoming duplicate files (e.g., notes_1.txt) instead of overwriting existing ones.

[ ] Daemon/Scheduler: Configure the script to run quietly in the background at a scheduled time every day.

📄 License

This project is open-source and available under the MIT License
