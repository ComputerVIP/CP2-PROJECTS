from chse_file import choose

def read():
    words = []
    file_path = choose()
    with open(file_path, 'r') as file:
        try:
            for line in file:
                words.extend(line.split()) #.extend makes it so every word is singular, .split splits where there is a space
                date = line.strip() #This updates every line to get the date written, because it is always at the end
            words.remove(date) #Removes the date to get an accurate word count
            print('Amount of words:\n    ', len(words)) #Prints the stats
            print('Last time edited:\n    ', date)
        except:
            print('File is empty!')
