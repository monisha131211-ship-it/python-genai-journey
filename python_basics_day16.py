import os
import shutil

folder = input("Enter folder path: ")

video_folder = os.path.join(folder, "Videos")
other_folder = os.path.join(folder, "Other_Files")

os.makedirs(video_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

videos = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path):
        extension = os.path.splitext(file)[1].lower()

        if extension in videos:
            shutil.move(path, video_folder)
        else:
            shutil.move(path, other_folder)

print("Files separated successfully!")
