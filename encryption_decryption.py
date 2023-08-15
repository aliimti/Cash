def check_integer_key():
    while True:
        cypher_key = input("Enter an integer key: ")
        if cypher_key.isdigit():
            cypher_key = int(cypher_key)
            return cypher_key
        else:
            print("Invalid input. Key must be an integer.")


def encrypting(character, cypher_key):
    original_character = ord(character)
    encrypted_character = original_character - cypher_key
    encrypted_character = chr(encrypted_character)
    return encrypted_character


def decrypting(encrypted_character, key):
    encrypted_character = ord(encrypted_character)
    decrypted_character = encrypted_character + key
    decrypted_character = chr(decrypted_character)
    return decrypted_character


def main():
    characters = input("Enter character or characters you want to encrypt: ")
    cypher_key = check_integer_key()
    encrypted_chars = [encrypting(iterate, cypher_key) for iterate in characters]
    encrypted_text = ''.join(encrypted_chars)
    print("After Encryption =", encrypted_text)

    print("DECRYPTION")
    cypher_key = check_integer_key()
    decrypted_characters = [decrypting(iterate, cypher_key) for iterate in encrypted_chars]
    decrypted_text = ''.join(decrypted_characters)
    print("After Decryption", decrypted_text)


if __name__ == "__main__":
    main()
