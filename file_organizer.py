import os
import shutil

# Folder to organize (change this later if needed)
SOURCE_FOLDER = "downloads"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def organize_files(folder):
    if not os.path.exists(folder):
        print(f"Folder '{folder}' does not exist.")
        return

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            for category, extensions in FILE_TYPES.items():
                if filename.lower().endswith(tuple(extensions)):
                    category_path = os.path.join(folder, category)

                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    break

    print("Files organized successfully.")

if __name__ == "__main__":
    organize_files(SOURCE_FOLDER)
