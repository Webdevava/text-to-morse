MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def text_to_morse(text):
    #function to convert text into morse code
    morse = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + ' '
        else:
            morse += ' '
    return morse

def morse_to_text(morse):
    #function to convert morse code into text
    text = ''
    morse_code = morse.split(' ')
    for code in morse_code:
        if code in MORSE_CODE_DICT.values():
            text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(code)]
        else:
            text += ' '
    return text

# take input from user
input_text = input('Enter text to convert to Morse code: ')

# convert text to Morse code
morse = text_to_morse(input_text)
print('Morse code: ', morse)

# take input from user
input_morse = input('Enter Morse code to convert to text: ')

# convert Morse code to text
text = morse_to_text(input_morse)
print('Text: ', text)

