from crypto_utils import encrypt_file, decrypt_file

def menu():
    print("\nAdvanced Encryption Tool (AES-256)")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "1":
            file_path = input("Enter file path to encrypt: ")
            password = input("Enter password: ")
            encrypt_file(file_path, password)
            print("File encrypted successfully.")

        elif choice == "2":
            file_path = input("Enter .enc file path to decrypt: ")
            password = input("Enter password: ")
            decrypt_file(file_path, password)
            print("File decrypted successfully.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
