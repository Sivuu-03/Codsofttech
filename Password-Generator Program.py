import random
import string

def generate_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lower_case + upper_case + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("The password length should be at least 1.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
