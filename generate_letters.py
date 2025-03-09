import string
import os

# Bright, child-friendly colors
COLORS = [
    "#FF9999", "#99FF99", "#9999FF", "#FFFF99", "#FF99FF", "#99FFFF",
    "#FFB366", "#66FFB3", "#B366FF", "#FFFF66", "#FF66B3", "#66FFFF",
    "#FF8080", "#80FF80", "#8080FF", "#FFFF80", "#FF80FF", "#80FFFF",
    "#FFA64D", "#4DFFA6", "#A64DFF", "#FFFF4D", "#FF4DA6", "#4DFFFF",
    "#FF6666", "#66FF66", "#6666FF"  # Last color for Z
]

template = '''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
  <rect width="200" height="200" fill="{}"/>
  <text x="100" y="100" font-family="Comic Sans MS, Arial, sans-serif" font-size="120" text-anchor="middle" dominant-baseline="middle" fill="#FFFFFF" stroke="#000000" stroke-width="2">{}</text>
  <text x="100" y="160" font-family="Comic Sans MS, Arial, sans-serif" font-size="24" text-anchor="middle" dominant-baseline="middle" fill="#000000">Letter {}</text>
</svg>'''

# Create images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Generate SVG files for each letter
for i, letter in enumerate(string.ascii_uppercase):
    filename = f'static/images/letter_{letter.lower()}.svg'
    with open(filename, 'w') as f:
        f.write(template.format(COLORS[i], letter, letter))
