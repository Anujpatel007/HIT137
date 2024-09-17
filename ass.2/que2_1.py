from PIL import Image

import time

current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(generated_number)

# Load the image and modify pixels
image = Image.open('Chapter1.jpg')
pixels = list(image.getdata())
n=generated_number
upgraded_pixels = [(r + n, g + n, b + n) for r, g, b in pixels]
upgraded_image= Image.new(image.mode, image.size)
upgraded_image.putdata(upgraded_pixels)
upgraded_image.save('chapter1out.jpg')

# Calculate sum of red pixel values
red_sum = sum([r for r, g, b in upgraded_pixels])
print(f"Sum of red pixels: {red_sum}")

# Calculate sum of green pixel values
green_sum = sum([g for r, g, b in upgraded_pixels])
print(f"Sum of green pixels: {green_sum}")

# Calculate sum of blue pixel values
blue_sum = sum([b for r, g, b in upgraded_pixels])
print(f"Sum of blue pixels: {green_sum}")