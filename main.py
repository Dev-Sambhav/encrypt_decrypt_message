import os
# import the logo
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['0','1','2','3','4','5','6','7','8','9']
def caesar(start_text,shift,direction):
  final_text =""
  if (direction == "decode"):
    shift *= -1
  for char in start_text:
    if(char == ' ' or (char in number)):
      final_text += char
    else:
      pos = alphabet.index(char) + shift
      final_text += alphabet[pos]
  print(f"\nHere's the {direction}d result: {final_text}")

while True:
  os.system("cls")
  print(logo);
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("\nType your message:\n").lower()
  shift = int(input("\nType the shift number:\n"))
  if(shift>26):
    shift = round(shift % 26)
  caesar(text,shift,direction)
  user_choice = input("\nType 'yes' if you want to go again. Otherwise type 'no'. ")
  if(user_choice.lower()=="yes"):
    continue
  else:
    break