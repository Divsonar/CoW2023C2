from PIL import Image, ImageDraw

# Read coordinates from the text file
with open("output.txt", "r") as file:
    coordinates_text = file.read()

# Parse coordinates
coordinates = [tuple(map(int, line.split(','))) for line in coordinates_text.strip().split('\n')]

# Find the dimensions of the image based on the coordinates
max_x = max(coord[0] for coord in coordinates)
max_y = max(coord[1] for coord in coordinates)

# Create a new image
image = Image.new("RGB", (400, 300), "white")
draw = ImageDraw.Draw(image)

# Draw points on the image
for coord in coordinates:
    draw.point(coord, fill="black")

# Save the image
image.save("output_image.png")

# Display the image
image.show()