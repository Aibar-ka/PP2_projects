import os

def check_access(path):

    if not os.path.exists(path):
        print("Path does not exist.")
        return

    print("Path exists.")

    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not Readable")

    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not Writable")

    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not Executable")

path = input("Enter the path to check access: ")
check_access(path)
