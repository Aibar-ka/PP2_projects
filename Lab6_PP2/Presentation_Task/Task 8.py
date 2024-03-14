import os


def delete_file(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File '{file_path}' does not exist.")
            return

        # Check for access
        if not os.access(file_path, os.R_OK | os.W_OK):
            print(f"No permission to delete file '{file_path}'.")
            return

        # Delete the file
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")


file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)
