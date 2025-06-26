def shift_letter(letter, shift):
    if letter == " ":
        return " "
    return chr((ord(letter) - ord("A") + shift) % 26 + ord("A")) 

def caesar_cipher(message, shift):
    result = ""
    for character in message:
        if character == " ":
            result += " "
        else:
            position = ord(character) - ord("A")
            new_position = (position + shift) % 26
            new_character = chr(new_position + ord("A"))
            result += new_character
    return result

def shift_by_letter(letter, shift_letter_char):
    if letter == " ":
        return " "
    shift_value = ord(shift_letter_char) - ord("A")
    position = ord(letter) - ord("A")
    new_position = (position + shift_value) % 26
    return chr(new_position + ord("A"))

def shift_by_letter(letter, shift_letter_char):
    if letter == " ":
        return " "
    return chr((ord(letter) - ord("A") + (ord(shift_letter_char) - ord("A"))) % 26 + ord("A"))

def vigenere_cipher(message, key):
    result = []
    key_index = 0
    for char in message:
        shift_char = key[key_index % len(key)]
        result.append(shift_by_letter(char, shift_char))
        key_index += 1
    return ''.join(result)

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    result = ""
    columns = len(message) // shift
    for i in range(len(message)):
        result += message[(i // shift) + (columns * (i % shift))]
    return result

def scytale_decipher(message, shift):
    result = [""] * len(message)
    columns = len(message) // shift
    for i in range(len(message)):
        result[(i // shift) + (columns * (i % shift))] = message[i]
    return ''.join(result)

