# Brady Graham - Updated Final - Josh Updated
def print_menu():
    print('Menu\n'
          '-----\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit')


def encode(message):
    encoded = ""
    for digit in message:
        encoded += str((int(digit) + 3) % 10)

    return encoded


def decode(encoded_message):
    decoded = ''
    for digit in encoded_message:
        decoded += str((int(digit) - 3) % 10)
    return decoded


def main():
    encoded_message = 'hi'
    while True:

        print_menu()

        selection = int(input('Please enter an option: '))

        if selection == 1:
            message = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!\n')
            encoded_message = encode(message)
        elif selection == 2:
            if encoded_message == '-1':
                break
            print(f'The encoded value is {encoded_message}, and the original password is {decode(encoded_message)}.\n')
        elif selection == 3:
            break
        else:
            print('Input out of range')


main()
