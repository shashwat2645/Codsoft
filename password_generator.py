import random
import string

def generate_password(length):
    password = ''
    # Characters to choose from: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters to form the password
    for i in range(length):
        password += random.choice(characters) 
    return password

def main():
    print("\tWelcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of your password: "))
        while length < 8:
            print("Password length must be at least 8 characters")
            length = int(input("Please enter the length again: "))

        password = generate_password(length)
        print(f"\nYour generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")

if __name__ == "__main__":
    main()
