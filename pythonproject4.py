
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    print("----------------------------")
    length = int(input("Enter password length (min 8 characters): "))
    num_passwords = int(input("Enter number of passwords to generate: "))

    for i in range(num_passwords):
        password = generate_password(length)
        print(f"Password {i+1}: {password}")

if __name__ == "__main__":
    main()
