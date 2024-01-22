from pathlib import Path

def direc_list(list_dir):  #list_dir contains ['L', '/home/algol/ics32/lectures']
    myPath = Path(list_dir[1])
    for currentpath in myPath.iterdir():
        print(currentpath)



def main(Command):
    list_dir = Command.split()
    if len(list_dir) == 2:
        direc_list(list_dir)



if __name__ == "__main__":
    while True:
        Command = input("L to list the contents of the user specified directory (Q to quit)")
        if Command == 'Q':
            break
        elif Command.startswith('L'):
            main(Command)

