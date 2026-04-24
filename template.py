import os
from pathlib import Path
import logging

# Basic config basically tells how you want your logs to look and where they should go
# Imp parametrs
# 1. level ---> DEBUG --> Detailed info
#               INFO ---> General info
#               WARNING --> Something odd
#               ERROR --> Something Failed
#               CRITICAL --> Serious error

# 2. Format ---> Define how logs look
#        '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.INFO,format='[%(asctime)s: %(message)s:]')

project_name="cnnClassifier"

# .github/workflows/ folder --> Folder used by git for
#                               GitHub Actions(CI/CD automation)
#                   Run tests automatically
#                   Deploy your app
#                   Train models
#                   Run scripts on push

# .gitkeep is just an empty placeholder file 
#                   Add .gitkeep so Git tracks the folder
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py"
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]
# Loop through a list of file paths
# filepath = Path(filepath) ---> convert string path into object using pathlib

# filedir, filename = os.path.split(filepath)
#  --> split path into : directory(folder)
#                      :file name

# filepath = "data/train/file1.csv" ----> filedir  = "data/train"
#                                         filename = "file1.csv"

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename=os.path.split(filepath)

# For each file path → convert it → then separate it into folder path and file name

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the file : {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w")as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} already exits")

# “If the folder doesn’t exist, create it. Then, if the file doesn’t 
# exist or is empty, create it. Otherwise, do nothing.”