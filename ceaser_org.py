alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def ceaser(text, shift, direction):

    cypher_text = ""

    for letter in text:
        position = alphabet.index(letter)

        if direction == 'encode':
            new_position = (shift + position) % len(alphabet)

        elif direction == 'decode':
            new_position = (position - shift) % len(alphabet)

        cypher_text += alphabet[new_position]

    return cypher_text


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(ceaser(text, shift, direction))
        break
    else:
        print("Invalid direction please retry giving your input!")