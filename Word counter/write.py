from datetime import datetime

def write():
    content = []
    with open('Word counter/doc.txt', 'r') as file:
        for row in file: #For every row in the file
            print(row)
            content.append(row.strip("\n")) #Adds the row, but removes newline
    with open('Word counter/doc.txt', 'w') as file:
        words = input('What would you like to write?\n') #Asks what they want to write
        content[0] = content[0] + " " + words + '\n' #Adds the writing, then a newline
        content[1] = datetime.now().strftime('%Y-%m-%d--%H:%M:%S') #Adds the exact date written... to the second
        for item in content:
            file.write(item) #Writes to the file
    with open('Word counter/doc.txt', 'r') as file: #Checks from the file to be sure everything got put in correctly
        for row in file:
            print(row)