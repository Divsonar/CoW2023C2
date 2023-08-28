from PIL import Image, ImageDraw
with open("output.txt", "r") as file:
    coordinates_text = file.read()
coordinates = [tuple(map(int, line.split(','))) for line in coordinates_text.strip().split('\n')]
image = Image.new("RGB", (400, 300), "white")
draw = ImageDraw.Draw(image)
for coord in coordinates:
    draw.point(coord, fill="black")
image.save("output_image.png")
image.show()