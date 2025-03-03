#Vincent Johnson, Word Counter
'''
Write a program that look at a document that a user has written on and update it with the word count and a timestamp for when that wordcount was last updated

REQUIREMENTS:

    Uses at least 3 pages (main, file handling, and time handling) NOTE: main is the only file name I've given you
    Reads and Writes to the file
    Uses functional decomposition
    Lets the user tell what file to use it on
    Uses good naming practices
    Has good white space
'''

from count import read as r
from write import write as w


def main(repeat):
    try:
        ans = int(input('''

What would you like to do?
    Write to the document(1)
    See when last updated, and see the word count(2)
    Exit(3)
''')) #asks what they want to do
    except ValueError: #Error handling
        ans = 4

    if ans == 1: #Goes to the correct place based on input
        w()
    elif ans == 2:
        r()
    elif ans == 3:
        print('Goodbye!')
        return 0 #makes the repeat variable 0
    else:
        print('Invalid input!')
    return repeat

if __name__ == '__main__': #Makes sure the program only runs when it's main
    repeat = 1
    while repeat > 0:
        repeat = main(repeat)