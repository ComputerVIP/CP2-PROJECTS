#Vincent Johnson- Morse Code Translator

#Repeat variable
rpt = 1

#Dictionary of the items
code = {
  'A': '.-',
  'B': '-...',
  'C': '-.-.',
  'D': '-..',
  'E': '.',
  'F': '..-.',
  'G': '--.',
  'H': '....',
  'I': '..',
  'J': '.---',
  'K': '-.-',
  'L': '.-..',
  'M': '--',
  'N': '-.',
  'O': '---',
  'P': '.--.',
  'Q': '--.-',
  'R': '.-.',
  'S': '...',
  'T': '-',
  'U': '..-',
  'V': '...-',
  'W': '.--',
  'X': '-..-',
  'Y': '-.--',
  'Z': '--..',
  ' ': '   ',
  '1': '.----',
  '2': '..---',
  '3': '...--',
  '4': '....-',
  '5': '.....',
  '6': '-....',
  '7': '--...',
  '8': '---..',
  '9': '----.',
  '0': '-----',
  '.': '.-.-.-',
  ',': '--..--',
  '?': '..--..',
  '\'': '.----.',
  '!': '-.-.--',
  '/': '-..-.',
  '(': '-.--.',
  ')': '-.--.-',
  '&': '.-...',
  ':': '---...',
  ';': '-.-.-.',
  '=': '-...-',
  '+': '.-.-.',
  '-': '-....-',
  '_': '..--.-',
  '"': '.-..-.',
  '$': '...-..-',
  '@': '.--.-.'
}

#This function uses a for loop to get the corresponding character in the dictionary and add it to a list
def translate1(code, rpt):
  txt = input("Enter text to be translated:\n")
  txt = txt.upper()

  #The list is here!
  a = list(txt)
  snt = []
  for i in a:
    if i in code:
      #Next list here!
      snt.append(code[i])
    else:
      pass
  print(snt)
  return code, rpt

#This runs the menu
def main(code, rpt):
  ans = input("What would you like to do?\n1 for translate to morse code\n2 for exit\n    ")
  if ans == "1":
    code, rpt = translate1(code, rpt)
    pass
  else:
    rpt = 0
    pass
  return code, rpt

while rpt > 0:
  code, rpt = main(code, rpt)