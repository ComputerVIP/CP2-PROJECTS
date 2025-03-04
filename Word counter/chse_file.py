import os

def new(directory):
    file_name = input('What would you like to name your file?\n')
    new_file_path = os.path.join(directory, file_name)

    try:
        # Open the file in 'x' mode to create a new file (raises error if exists)
        with open(new_file_path, 'x') as new_file:
            new_file.write('')
        print(f'File created successfully: {new_file_path}')
        return new_file_path
    except FileExistsError:
        print(f'The file "{new_file_path}" already exists!')
        return None

def choose():
    home_dir = os.path.expanduser('~')  # Get home directory
    directories = {
        'downloads': os.path.join(home_dir, 'Downloads'),
        'documents': os.path.join(home_dir, 'Documents')
    }

    # Ask the user to choose a folder
    choice = input('Choose a folder (downloads/documents):\n').strip().lower()
    script_folder = directories.get(choice)

    if not script_folder or not os.path.exists(script_folder):
        print('Invalid choice or directory does not exist.')
        return None

    print(f'Selected directory: {script_folder}')

    # Search for all .txt files in the folder and subfolders
    txt_files = []
    for root, _, files in os.walk(script_folder):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))

    if txt_files:
        print('Available files:')
        for idx, file in enumerate(txt_files, 1):
            print(f'    {idx}. {file}')

        # Let the user choose a file by index (or create a new file)
        try:
            selected_idx = int(input(f'Choose a file by number, or enter {len(txt_files)+1} to create a new file:\n')) - 1
        except ValueError:
            print('Invalid input. Please enter a number.')
            return None

        if selected_idx == len(txt_files):  # If they choose to create a new file
            return new(script_folder)  

        if 0 <= selected_idx < len(txt_files):  # If a valid index is selected
            return txt_files[selected_idx]
        else:
            print('Invalid selection.')
            return None
    else:
        print('No .txt files found. Creating a new file.')
        return new(script_folder)