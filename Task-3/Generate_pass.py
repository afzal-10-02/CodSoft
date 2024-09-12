import random
import string

def main():
    num = int(input("Enter the length of the Password : "))
    special = input('Want to use Special Case (yes/no): ').lower()
    if num<8:
        print("Length must be Greater than or equal to 8.")
    else:
        if special == 'no':
            print(f'Random Generated Password is : {generate_password(length=num, use_special_chars =False)}')
        else:
            print(f'Random Generated Password is : {generate_password(length=num)}')

def generate_password(length=8, use_special_chars=True):

    digits = string.digits
    letters = string.ascii_letters
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = digits + letters + special_chars

    if not all_chars:
        raise ValueError("At least one character set must be included.")

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

if __name__ == "__main__":
    main()