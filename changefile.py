import shutil,os,glob

# setting up destination folders

PYDEST = "/home/ubuntu/python-scripts/python-test"

TEXTDEST = "/home/ubuntu/python-scripts/texte-test"

def move8files(pwd):
    PWD = pwd + "*"
    for files in glob.glob(PWD):
        if files.endswith(".txt"):
            print(files)
            shutil.move(files,TEXTDEST)
        elif files.endswith(".py"):
            shutil.move(files,PYDEST)

move8files("/home/ubuntu/python-scripts/")
