from datetime import datetime
from chse_file import choose


def write():
    print('\n\n')
    content = ['','']
    cnt = 0
    file_path = choose()
    with open(file_path, 'r') as file:
        for row in file: #For every row in the file
            print(row)
            content[cnt] = row.strip("\n") #Adds the row, but removes newline
            cnt += 1

    with open(file_path, 'w') as file:
        words = input('What would you like to write?\n') #Asks what they want to write
        content[0] = content[0] + ' ' + words #Adds the writing, then a newline
        content[0] = content[0].strip() + '\n'
        content[1] = datetime.now().strftime('%Y-%m-%d--%H:%M:%S') #Adds the exact date written... to the second

        for item in content:
            file.write(item) #Writes to the file
    with open(file_path, 'r') as file: #Checks from the file to be sure everything got put in correctly
        print('\nFile contents:')
        for row in file:
            print(row)