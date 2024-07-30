import os
import re
import subprocess
import sys
import tkinter as tk
from tkinter import ttk

def parseVersion(version_string):
    return tuple(map(int, re.findall(r"\d+", version_string)))

def openDirectory(file_path, argument=None):
    if os.path.exists(file_path):
        if argument:
            subprocess.Popen([file_path, argument])
        else:
            os.startfile(file_path)
    else:
        tk.messagebox.showerror("Error", f"File not found: {file_path}")
    root.quit()


def findDesignerExe(program_files_dir, folder_name):
    designer_executables = []
    target_dir = os.path.join(program_files_dir, folder_name)
    if os.path.exists(target_dir):
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            if os.path.isdir(item_path) and "Designer" in item:
                executable_path = os.path.join(item_path, "Q-Sys Designer.exe")
                if os.path.exists(executable_path):
                    designer_executables.append(executable_path)
    return designer_executables


def getVersionFromFile(file_path):
    try:
        with open(file_path, "rb") as file:  
            content = file.read()
            version_match = re.search(rb"Version=(\d+(\.\d+)*)", content)
            if version_match:
                return version_match.group(1).decode("utf-8")
    except Exception as e:
        print(f"Error reading file: {e}")
    return ""


# Main
if len(sys.argv) > 1:
    file_path = ' '.join(sys.argv[1:])
    version_number = getVersionFromFile(file_path)
else:
    version_number = ""
    file_path = None

program_files_dir = os.environ.get("PROGRAMFILES", " ")
program_files_x86_dir = os.environ.get("PROGRAMFILES(x86)", " ")

designer_executables = []
if program_files_dir:
    designer_executables.extend(findDesignerExe(program_files_dir, "QSC"))
if program_files_x86_dir:
    designer_executables.extend(findDesignerExe(program_files_x86_dir, "QSC Audio"))

designer_executables.sort(key=lambda x: parseVersion(re.search(r"\d+\.\d+", os.path.basename(os.path.dirname(x))).group()))

root = tk.Tk()
root.title("Q-SYS Launcher")
root.minsize(300, 100)
root.iconbitmap('Res/Icon.ico')

if version_number:
    version_label = ttk.Label(root, text=f"Version from file: {version_number}", font=("Arial", 14))
    version_label.pack(padx=10, pady=3)

max_button_width = max([len(os.path.basename(os.path.dirname(exe_path))) for exe_path in designer_executables], default=0)

for index, exe_path in enumerate(designer_executables):
    dir_name = os.path.basename(os.path.dirname(exe_path))
    button = tk.Button(root, text=dir_name, width=max_button_width, command=lambda path=exe_path: openDirectory(path, file_path))
    button.pack(padx=20, pady=3)

root.mainloop()
