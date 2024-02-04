# Project
# Ceasar Cipher - shifts the letters of the alphabet by a secret number to encode
# or decode a specific text
import os
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher():
  """Here's the docstring!"""
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  def ceasar(direction, entered_text, shift_amount):
    final_text = ""
    if direction == "decode":
      shift_amount *= -1
    for char in entered_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        final_text += alphabet[new_position]
      else:
        final_text += char
    print(f"The {direction}d text is {final_text}")

  ceasar(direction=direction, entered_text=text, shift_amount=shift)
  rerun = input("Do you want to run the cipher again? Type yes or no.\n")
  if rerun == "yes":
    os.system('clear')
    cipher()
  elif rerun == "no":
    print("Goodbye!")
    exit()


print(logo)
cipher()
