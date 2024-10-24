#Brady Graham - Updated
def printMenu():
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

def main():
    while True:

        printMenu()

        selection = int(input('Please enter an option: '))

        if selection == 1:
            message = input('Please enter your password to encode: ')
        elif selection == 2:
            print(f'the encoded value is')
        elif selection == 3:
            break
        else:
            print('Input out of range')

main()
