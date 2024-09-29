from django.shortcuts import render

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

inverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def text_to_morse(text):
    return ' '.join(morse_code_dict.get(char, '') for char in text.upper())

def morse_to_text(morse_code):
    words = morse_code.split('  ')
    decoded_words = [''.join(inverse_morse_code_dict.get(char, '') for char in word.split()) for word in words]
    return ' '.join(decoded_words)

def translator(request):
    encoded_morse = ''
    decoded_text = ''

    if request.method == 'POST':
        if 'encode_data' in request.POST:
            text = request.POST.get('encode_data')
            encoded_morse = text_to_morse(text)
        elif 'decode_data' in request.POST:
            morse_code = request.POST.get('decode_data')
            decoded_text = morse_to_text(morse_code)

    return render(request, 'home.html', {'encoded_morse': encoded_morse, 'decoded_text': decoded_text})
