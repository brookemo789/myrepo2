def print_menu():
    print("\nMenu")
    print("-------------")
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

def encode(og_password):
    encoded_password = ''
    for i in range(len(og_password)):
        encoded_password += str((int(og_password[i]))+3)
    return encoded_password

def decode(encoded_password = "12345555"):
    og_password = ''
    for i in range(len(encoded_password)):
        og_password += str((int(encoded_password[i])) -3)
    return og_password

if __name__ == '__main__':
    loop = True
    while loop:
        print_menu()
        user_choice = int(input("Please enter an option: "))

        if user_choice == 1:
            og_password = input("Pleae enter your password to encode: ")
            encoded_password = encode(og_password)
            print('Your password has been encoded and stored!')
        elif user_choice == 2:
            og_password = decode(encoded_password)
            print('The encoded password is ' + str(encoded_password) + ', and the original password is ' + str(og_password) + '.')
        elif user_choice == 3:
            break
