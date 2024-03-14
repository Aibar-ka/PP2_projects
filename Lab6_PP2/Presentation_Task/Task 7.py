def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = input("Enter the path to the source file: ")
destination_file = input("Enter the path to the destination file: ")

copy_file(source_file, destination_file)
