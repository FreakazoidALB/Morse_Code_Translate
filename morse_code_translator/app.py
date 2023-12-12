from flask import Flask, render_template, request

# Create a Flask web application instance
app = Flask(__name__, static_url_path='/static')

# Define a dictionary for Morse code translation
morse_code_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char
    return morse_code.strip()

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission and Morse code translation
@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        # Get input text from the form
        input_text = request.form['input_text']
        # Convert input text to Morse code
        morse_code = text_to_morse(input_text)
        # Render the main page with the input text and Morse code
        return render_template('index.html', input_text=input_text, morse_code=morse_code)

# Run the Flask app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
