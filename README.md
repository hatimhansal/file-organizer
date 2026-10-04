File Organizer

A simple and lightweight Python tool that automatically organizes files into folders based on their file extensions.

📌 Overview

File Organizer helps keep your folders clean and organized by automatically sorting files into categories such as:

- Images
- Videos
- Documents
- Code
- Archives
- Others

The project is built with Python using "pathlib" and "shutil".

✨ Features

- Automatically detects file extensions.
- Organizes files into categorized folders.
- Supports common image, video, document, code, and archive formats.
- Creates category folders automatically when needed.
- Handles files with unknown extensions using an "Others" folder.
- Prevents filename conflicts by automatically renaming duplicate files.
- Simple and lightweight.

🛠️ Technologies

- Python 3
- "pathlib"
- "shutil"

📂 Supported File Types

Category| Extensions
Images| ".jpg", ".jpeg", ".png", ".gif"
Videos| ".mp4", ".mkv", ".avi"
Documents| ".pdf", ".docx", ".txt"
Code| ".py", ".js", ".html", ".css"
Archives| ".zip", ".rar"
Others| Other file extensions

🚀 How It Works

The program scans a selected folder and checks the extension of each file.

For example:

photo.jpg  → Images/
movie.mp4  → Videos/
book.pdf   → Documents/
script.py  → Code/
archive.zip → Archives/
unknown.xyz → Others/

If a file with the same name already exists, the program automatically creates a new name:

photo.jpg
photo_1.jpg
photo_2.jpg

▶️ Usage

Clone the repository:

git clone https://github.com/YOUR_USERNAME/file-organizer.git
cd file-organizer

Run the program:

python main.py

By default, the current version can be configured to organize a folder such as:

~/Videos

📁 Example

Before:

Videos/
├── photo.jpg
├── movie.mp4
├── book.pdf
├── script.py
└── archive.zip

After:

Videos/
├── Images/
│   └── photo.jpg
├── Videos/
│   └── movie.mp4
├── Documents/
│   └── book.pdf
├── Code/
│   └── script.py
└── Archives/
    └── archive.zip

🎯 Project Goal

This project was created as a practical Python project to learn:

- "pathlib"
- Lists
- Dictionaries
- Functions
- Loops
- Conditions
- File handling
- Working with the filesystem
- Using external Python modules

The goal is to gradually improve the project while learning Python through real-world development.

🔮 Future Improvements

Planned improvements include:

- Command-line arguments
- Support for more file extensions
- Custom folder selection
- Dry-run mode
- Better error handling
- Configuration file
- Logging
- Undo functionality
- Interactive CLI interface

👨‍💻 Author

Created by Hatim as a practical Python learning project.

---

⭐ If you find this project useful, feel free to star the repository.