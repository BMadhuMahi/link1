import string
import random


def generate_password(length):
    # Define character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + symbols

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all characters
    if length > 4:
        password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)


def main():
    print("Password Generator")

    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password (minimum 4 characters): "))

    # Ensure the length is at least 4 to include all character types
    if length < 4:
        print("Password length must be at least 4 characters.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
"# link" 
