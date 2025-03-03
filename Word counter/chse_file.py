import os

def new():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    new_file_path = os.path.join(script_folder, input('What would you like to name your file?\n'))
    try:
        # Open the file in 'x' mode to create a new file (raises error if exists)
        with open(new_file_path, 'x') as new_file:
            new_file.write('')
            print(f'File: {new_file_path} \nwas created successfully.')
    except FileExistsError:
        print(f'The file {new_file_path} already exists!')
        return
    return new_file_path

def choose():
    # Get the path of the current script folder (Word Counter inside CP)
    script_folder = os.path.dirname(os.path.abspath(__file__))

    # List all .txt files in the current folder (Word Counter)
    txt_files = [f for f in os.listdir(script_folder) if f.endswith(".txt")]

    if txt_files: #If there are txt files
        # Print the list of txt files (you can display it to the user)
        print('Available files:')
        for idx, file in enumerate(txt_files, 1):
            print(f"    {idx}. {file}")

        # Let the user choose a file by index (or choose programmatically)
        try:
            selected_idx = int(input(f'Choose a file by number, if you want to create a new file, enter {len(txt_files)+1}\n')) - 1
        except:
            selected_idx = 0

        if selected_idx == (len(txt_files) + 1): #If they choose to make a new file
            new()
        selected_file = txt_files[selected_idx] #Selects file

        # Now open the selected file
        file_path = os.path.join(script_folder, selected_file)
    else: #If there are no txt files
        file_path = new() #Makes a new txt file and keeps directory

        if file_path: #If there is an actual path
            pass
        else: #If not
            return
    return file_path