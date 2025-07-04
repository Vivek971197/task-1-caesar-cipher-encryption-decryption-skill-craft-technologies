def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"\n{mode.capitalize()}ed message: {result}")

if __name__ == "__main__":
    main()
