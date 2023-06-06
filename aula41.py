import os

secretWord = "Pimenta"
lettersOk = ''
attempts = 0

while True:
  letter = input("Digite uma letra: ")
  attempts += 1
  
  if len(letter) > 1 :
    print("Digite apenas 1 letra")
    continue

  if letter in secretWord:
    lettersOk += letter

  wordOk = ''
  for secretLetter in secretWord:
    if secretLetter in lettersOk:
      wordOk += secretLetter
    else:
      wordOk += "*"

  print(wordOk)

  if secretWord == wordOk:      
    os.system('clear')
    print('A palavra secreta é', wordOk ,'e o tentou', attempts, 'vezes')
    lettersOk = ''
    attempts = 0
