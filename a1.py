from pathlib import Path

def direc_list(myPath):  #list_dir contains ['L', '/home/algol/ics32/lectures']
    for currentpath in myPath.iterdir():
        print(currentpath)


def recursive_list(myPath):
    for currentpath in myPath.iterdir():
        if currentpath.is_file():
            print(currentpath)
        elif currentpath.is_dir():
            print(currentpath)
            recursive_list(currentpath)

def only_files(myPath):
    for currentpath in myPath.iterdir():
        if currentpath.is_file():
            print(currentpath)

def file_search(myPath, filename):  #change the variable to filename
    for currentpath in myPath.iterdir():
        if currentpath.is_file() and currentpath.name.lower() == filename.lower():
            print(currentpath)

def main(Command):
    list_dir = Command.split()
    myPath = Path(list_dir[1])
    if len(list_dir) == 2:
        direc_list(list_dir, myPath)
    elif len(list_dir) == 3:
        if list_dir[2] == '-r':
            recursive_list(myPath)
        elif list_dir[2] == '-f':
            only_files(myPath)
    elif len(list_dir) == 4:
        if list_dir[2] == '-s':
            filename = list_dir[3]
            file_search(myPath, filename)
        elif list_dir[2] == '-e':
            ext = list_dir[3]
            search_by_extension(myPath, ext)


if __name__ == "__main__":
    while True:
        Command = input("L to list the contents of the user specified directory (Q to quit)")
        if Command == 'Q':
            break
        elif Command.startswith('L'):
            main(Command)

