from flask import Flask, render_template, jsonify, request, send_file
from gtts import gTTS
import os
import tempfile

app = Flask(__name__)

# Ensure the audio directory exists
os.makedirs('static/audio', exist_ok=True)
os.makedirs('static/images', exist_ok=True)

# Simple word database with categories
WORDS = {
    'animals': [
        {'word': 'cat', 'image': 'cat.png'},
        {'word': 'dog', 'image': 'dog.png'},
        {'word': 'bird', 'image': 'bird.png'},
    ],
    'food': [
        {'word': 'apple', 'image': 'apple.png'},
        {'word': 'banana', 'image': 'banana.png'},
        {'word': 'milk', 'image': 'milk.png'},
    ],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_words')
def get_words():
    category = request.args.get('category', 'animals')
    return jsonify(WORDS.get(category, []))

@app.route('/get_audio/<word>')
def get_audio(word):
    try:
        # Create a temporary file for the audio
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
            tts = gTTS(text=word, lang='en', slow=True)
            tts.save(temp_file.name)
            return send_file(temp_file.name, mimetype='audio/mpeg')
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    os.makedirs('static/audio', exist_ok=True)
    app.run(debug=True)
