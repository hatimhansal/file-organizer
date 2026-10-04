from pathlib import Path
import shutil

categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".zip": "Archives",
    ".rar": "Archives",
}


def get_files(place):
    folder = Path.home() / place
    list_items = folder.iterdir()
    list_files = []

    for item in list_items:
        if item.is_file():
            list_files.append(item)

    return list_files


folder = Path.home() / "Videos"
tableau_file = get_files("Videos")

print(f"Organizing: {folder}")

for file in tableau_file:

    extension = file.suffix.lower()

    if extension in categories:
        category = categories[extension]
    else:
        category = "Others"

    destination = folder / category
    destination.mkdir(exist_ok=True)

    new_file = destination / file.name

    if new_file.exists():
        print(f"Already exists: {new_file}")

        counter = 1

        while new_file.exists():
            new_file = destination / f"{file.stem}_{counter}{file.suffix}"
            counter += 1

    shutil.move(file, new_file)

    print(f"{file.name} -> {new_file}")