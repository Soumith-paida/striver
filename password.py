import random
import string

def generate_password(length, complexity):
    """Generates a random password based on the given length and complexity.

    Args:
        length: The desired length of the password.
        complexity: A string indicating the desired complexity (e.g., 'weak', 'medium', 'strong').

    Returns:
        A randomly generated password string.
    """

    if complexity == 'weak':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Please choose 'weak', 'medium', or 'strong'.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to interact with the user and generate passwords."""

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            complexity = input("Enter the desired complexity (weak, medium, strong): ")
            password = generate_password(length, complexity)
            print("Generated password:", password)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for length and a valid complexity level.")

if __name__ == "__main__":
    main()