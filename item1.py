
def caesar_cipher(m, N):
    # Initialize an empty string to store the ciphertext
    ciphertext = ""

    # Check if N is an integer (Caesar cipher)
    if isinstance(N, int):
        # Iterate over each character in the message
        for char in m:
            # Check if the character is a letter
            if char.isalpha():
                # Determine the starting point based on the character's case
                if char.isupper():
                    start = ord('A')  # ASCII value of 'A'
                else:
                    start = ord('a')  # ASCII value of 'a'

                # Apply the Caesar cipher shift to the character
                shifted = (ord(char) - start + N) % 26 + start

                # Append the shifted character to the ciphertext
                ciphertext += chr(shifted)
            else:
                # Non-letter characters are left unchanged
                ciphertext += char

    # Check if N is a dictionary (direct substitution)
    elif isinstance(N, dict):
        # Iterate over each character in the message
        for char in m:
            # Check if the character is present in the substitution dictionary
            if char.upper() in N:
                # Preserve the case of the original character and substitute with the corresponding value  # noqa
                if char.isupper():
                    ciphertext += N[char.upper()].upper()
                else:
                    ciphertext += N[char.upper()].lower()
            else:
                # If the character is not in the dictionary, leave it unchanged
                ciphertext += char

    # If N is neither an integer nor a dictionary, raise an error
    else:
        raise ValueError("Invalid input for N. N should be an integer or a dictionary.")  # noqa

    # Return the final ciphertext
    return ciphertext
