import sys
# Caesar Cipher function
def caesar(message, shift):
    result = ""
    for ch in message:
        if ch.isupper():
            # Shift uppercase letters
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            # Shift lowercase letters
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            # Keep spaces and special characters unchanged
            result += ch
    return result

# Check for command-line input
if len(sys.argv) >= 3:
    message = sys.argv[1]
    shift = int(sys.argv[2])
    print("Encrypted:", caesar(message, shift))
    print("Decrypted:", caesar(message, -shift))

# Otherwise take input from the user
else:
    message = input("Enter message: ")
    shift = int(input("Enter shift: "))
    choice = input("Enter E for Encryption or D for Decryption: ").upper()

    if choice == "E":
        print("Encrypted:", caesar(message, shift))

    elif choice == "D":
        print("Decrypted:", caesar(message, -shift))
    # Invalid choice
    else:
        print("Invalid choice!")