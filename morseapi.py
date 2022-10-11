MORSE = {'!': "-.-.--", '"': ".-..-.", '$': "...-..-", '&': ".-...", "'": ".----.",
         '(': "-.--.", ')': "-.--.-", '+': ".-.-.", ',': "--..--", '-': "-....-",
         '.': ".-.-.-", '/': "-..-.", '0': "-----", '1': ".----", '2': "..---", '3': "...--",
         '4': "....-", '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.",
         ':': "---...", ';': "-.-.-.", '=': "-...-", '?': "..--..", '@': ".--.-.", '_': "..--.-",
         'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.",
         'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--",
         'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
         'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--..", ' ': "/"}

def encode(text):
    text = text.strip()
    z = ''
    for i in range(len(text)):
        for c, k in MORSE.items():
            if text[i].upper() == c.upper(): z += k + " "

    return z

def decode(text):
    text = text.strip()
    z = ''
    for i in text.split(" "):
        for c,k in MORSE.items():
            if i.upper().strip() == k.upper(): z += c
    return z
