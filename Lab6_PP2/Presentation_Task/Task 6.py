import string

def generate_files():
    try:
        for letter in string.ascii_uppercase:
            file_name = f"{letter}.txt"
            with open(file_name, 'w') as file:
                file.write(f"This is file {file_name}.")
            print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

generate_files()
