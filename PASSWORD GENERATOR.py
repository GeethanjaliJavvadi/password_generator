#import requried modules

import random

import string

#define fnction to generate password

def generate_password(length=8):
    
# Generate a random password of given length.
    
    characters_in_password = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters_in_password) 
                       for _ in range(length))
    return password

#define the function to enter the lenght of the password

def main():
    password_size = int(input("Enter the size of the password: "))
    password = generate_password(password_size)
    print("Generated Password:", password)
    return

if __name__ == "__main__":
    main()