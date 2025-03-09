import os

# Bright, child-friendly colors with good contrast
COLORS = {
    0: "#FF99CC",  # Pink
    1: "#99FF99",  # Light Green
    2: "#99CCFF",  # Light Blue
    3: "#FFCC99",  # Light Orange
    4: "#CC99FF",  # Light Purple
    5: "#99FFCC",  # Mint
    6: "#FFB366",  # Orange
    7: "#66B3FF",  # Blue
    8: "#FF66B3",  # Dark Pink
    9: "#B366FF",  # Purple
    10: "#66FFB3", # Seafoam
    11: "#FF9999", # Light Red
    12: "#99FF99", # Light Green
    13: "#9999FF", # Light Blue
    14: "#FFFF99", # Light Yellow
    15: "#FF99FF", # Light Purple
    16: "#99FFFF", # Light Cyan
    17: "#FFB366", # Light Orange
    18: "#66FFB3", # Light Mint
    19: "#B366FF", # Light Violet
    20: "#FF66B3", # Light Pink
}

def generate_dots(num):
    if num == 0:
        return ""
    
    dots = []
    radius = 6 if num > 10 else 8  # Smaller dots for larger numbers
    
    if num <= 10:
        # Original pattern for 1-10
        if num <= 3:
            # Single row for 1-3
            start_x = 100 - (num * 20) + 20
            for i in range(num):
                dots.append(f'<circle cx="{start_x + i*40}" cy="140" r="{radius}" fill="black"/>')
        elif num <= 6:
            # Two rows for 4-6
            per_row = (num + 1) // 2
            for row in range(2):
                dots_in_row = min(per_row, num - row * per_row)
                start_x = 100 - (dots_in_row * 20) + 20
                for i in range(dots_in_row):
                    dots.append(f'<circle cx="{start_x + i*40}" cy="{130 + row*20}" r="{radius}" fill="black"/>')
        else:
            # Three rows for 7-10
            per_row = (num + 2) // 3
            for row in range(3):
                dots_in_row = min(per_row, num - row * per_row)
                start_x = 100 - (dots_in_row * 20) + 20
                for i in range(dots_in_row):
                    dots.append(f'<circle cx="{start_x + i*40}" cy="{120 + row*20}" r="{radius}" fill="black"/>')
    else:
        # For numbers 11-20, show 10 dots plus remaining dots in a special pattern
        # First, show 10 dots in a compact 2x5 grid
        for row in range(2):
            for col in range(5):
                dots.append(f'<circle cx="{60 + col*30}" cy="{125 + row*15}" r="{radius}" fill="black"/>')
        
        # Then show remaining dots (num - 10) in a row below
        remaining = num - 10
        start_x = 100 - (remaining * 15) + 15
        for i in range(remaining):
            dots.append(f'<circle cx="{start_x + i*30}" cy="155" r="{radius}" fill="black"/>')
    
    return "\n    ".join(dots)

template = '''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
  <rect width="200" height="200" fill="{}"/>
  <text x="100" y="80" font-family="Comic Sans MS, Arial, sans-serif" font-size="{}" text-anchor="middle" dominant-baseline="middle" fill="#FFFFFF" stroke="#000000" stroke-width="2">{}</text>
  {}
</svg>'''

# Create images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Generate SVG files for each number
for num in range(21):
    filename = f'static/images/number_{num}.svg'
    dots = generate_dots(num)
    # Use smaller font size for 2-digit numbers
    font_size = "80" if num >= 10 else "100"
    with open(filename, 'w') as f:
        f.write(template.format(COLORS[num], font_size, str(num), dots))
