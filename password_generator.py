import random
import string

letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation
uppercase_letter = string.ascii_uppercase

all_characters = letters + numbers + special_characters



def generate_password():
    password_length = int(input("Choose the length of the password: "))
    password = ''.join(random.choices(all_characters + uppercase_letter, k=password_length))

    print(password)


generate_password()
