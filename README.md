# Speech Learning Friend

A friendly web application designed to help children with Down Syndrome learn speech through interactive picture cards, audio pronunciation, and positive reinforcement.

## Features
- Simple, colorful interface designed for accessibility
- Picture cards with associated words
- Clear audio pronunciation with slower speech rate
- Categories for different types of words (animals, food)
- Interactive animations for engagement
- Touch-friendly interface

## Setup
1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open a web browser and navigate to `http://localhost:5000`

## Adding New Content
To add new words and pictures:
1. Add picture files to the `static/images` directory
2. Update the `WORDS` dictionary in `app.py` with new categories and words
