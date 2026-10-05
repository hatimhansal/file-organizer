📁 File Organizer

A simple and lightweight Python tool that automatically organizes files into categorized folders based on their file extensions.

The project was created as a practical Python learning project to understand file handling, filesystem operations, functions, loops, conditions, and Python modules such as "pathlib" and "shutil".

---

📌 Overview

File Organizer scans a selected directory, identifies files by their extensions, and automatically moves them into appropriate category folders.

For example:

photo.jpg     → Images/
movie.mp4     → Videos/
document.pdf  → Documents/
script.py     → Code/
archive.zip   → Archives/
unknown.xyz   → Others/

The goal is to make messy folders easier to manage while practicing real-world Python development.

---

✨ Features

- 📂 Automatically organizes files by extension
- 🖼️ Supports common image formats
- 🎬 Supports common video formats
- 📄 Supports common document formats
- 💻 Supports common programming files
- 🗜️ Supports common archive formats
- 📁 Creates category folders automatically
- ❓ Places unsupported file types in "Others/"
- 🔄 Prevents filename conflicts by generating unique filenames
- 🪶 Lightweight and easy to understand
- 🐍 Built with standard Python libraries

---

🛠️ Technologies

- Python 3
- "pathlib"
- "shutil"

No external Python packages are required for the core functionality.

---

📂 Supported File Types

Category| Extensions
🖼️ Images| ".jpg", ".jpeg", ".png", ".gif"
🎬 Videos| ".mp4", ".mkv", ".avi"
📄 Documents| ".pdf", ".docx", ".txt"
💻 Code| ".py", ".js", ".html", ".css"
🗜️ Archives| ".zip", ".rar"
📦 Others| Other or unsupported extensions

«More extensions can be added easily by modifying the project's category configuration.»

---

🚀 How It Works

The program follows a simple process:

1. 📂 Selects the folder to organize.
2. 🔍 Scans the files inside the folder.
3. 🧩 Checks each file's extension.
4. 🏷️ Determines the appropriate category.
5. 📁 Creates the category folder if necessary.
6. 🚚 Moves the file into the category folder.
7. 🔄 Generates a new filename if a conflict already exists.

Example

photo.jpg

becomes:

Images/
└── photo.jpg

And if "photo.jpg" already exists:

Images/
├── photo.jpg
├── photo_1.jpg
└── photo_2.jpg

---

▶️ Installation & Usage

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/file-organizer.git

2. Enter the project directory

cd file-organizer

3. Run the program

python main.py

The folder to organize can be configured in the Python source code.

For example:

~/Videos

---

📁 Example

Before

Videos/
├── photo.jpg
├── movie.mp4
├── book.pdf
├── script.py
└── archive.zip

After

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

---

🎯 Project Goals

This project was built as a practical way to learn and practice Python concepts, including:

- "pathlib"
- "shutil"
- Lists
- Dictionaries
- Functions
- Loops
- Conditions
- File handling
- Filesystem operations
- Modules
- Basic project structure

Instead of learning Python only through exercises, the project focuses on building something useful with real files and directories.

---

🔮 Future Improvements

The project will be gradually improved with features such as:

- [ ] Command-line arguments
- [ ] Custom folder selection
- [ ] Support for more file extensions
- [ ] Dry-run mode
- [ ] Better error handling
- [ ] Configuration file
- [ ] Logging system
- [ ] Undo functionality
- [ ] Interactive CLI
- [ ] Recursive folder organization
- [ ] Improved cross-platform support

---

📚 Learning Journey

This project is part of my journey to improve my Python programming and build practical software projects.

The project may start simple, but the goal is to progressively improve its structure, reliability, and features while learning new Python concepts.

---

👨‍💻 Author

Hatim

Created as a practical Python learning project.

---

⭐ Support

If you find this project useful or interesting, feel free to ⭐ star the repository.

Feedback and suggestions are welcome!