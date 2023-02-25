import random
import string

def generate_random_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

used_passwords = set()

# Generate random passwords indefinitely and write to a file
with open("random_passwords.txt", "w") as file:
    while True:
        random_password = generate_random_password(12)
        if random_password not in used_passwords:
            used_passwords.add(random_password)
            print(random_password)
            file.write(random_password + "\n")
