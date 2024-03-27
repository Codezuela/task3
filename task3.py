import string
import random

def generate_password(length, use_uppercase, use_numbers, use_punctuation):
    """Generate a password of the specified length and complexity."""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to run the password generator application."""
    print("Welcome to the password generator!")
    length = int(input("Enter the length of the password: "))
    use_uppercase = bool(input("Use uppercase letters (y/n): "))
    use_numbers = bool(input("Use numbers (y/n): "))
    use_punctuation = bool(input("Use punctuation (y/n): "))
    password = generate_password(length, use_uppercase, use_numbers, use_punctuation)
    print(f"Generated password: {password}")

if __name__ == '__main__':
    main()
