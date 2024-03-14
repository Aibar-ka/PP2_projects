def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List successfully written to '{file_path}'.")
    except Exception as e:
        print(f"Error occurred while writing to '{file_path}': {e}")

data = input("Enter the list (comma-separated): ").split(',')
file_path = input("Enter the path to save the file: ")

write_list_to_file(file_path, data)
