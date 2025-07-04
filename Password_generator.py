import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    try:
        
        password_length = int(input("Enter the desired password length: "))
        
        if password_length <= 0:
            print("Password length must be a positive integer.")
            return
        
        password = generate_password(password_length)
        
        print("Generated Password:", password)
        
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")

if __name__ == "__main__":
    main()
