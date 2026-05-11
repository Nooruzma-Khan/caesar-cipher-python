def caesar_encrypt(text, shift):
    shift = shift % 26  # normalize shift, handles >26 and negatives
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        elif char.isdigit():
            result += str((int(char) + shift) % 10)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def main():
    while True:
        print("\n--- Caesar Cipher ---")
        choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()

        if choice == 'Q':
            print("Goodbye!")
            break

        if choice not in ('E', 'D'):
            print("Invalid choice. Please enter E, D, or Q.")
            continue

        text = input("Enter the text (letters and numbers): ").strip()
        if not text:
            print("Text cannot be empty.")
            continue

        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid shift. Please enter an integer.")
            continue

        if choice == 'E':
            result = caesar_encrypt(text, shift)
            print("Encrypted text:", result)
        else:
            result = caesar_decrypt(text, shift)
            print("Decrypted text:", result)


main()


