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
# want to creat the same thing with the g and b and compair the output as like (r + n, g + n, b + n) for r
new_image = Image.new(image.mode, image.size)
new_image.putdata(upgraded_pixels)
new_image.save('chapter1out.jpg')

# Calculate sum of red pixel values
red_sum = sum([r for r, g, b in upgraded_pixels])
print(f"Sum of red pixels: {red_sum}")

green_sum = sum([ g for r, g, b in upgraded_pixels])
print(f"Sum of green pixels: {green_sum}")

blue_sum = sum([ b for r, g, b in upgraded_pixels])
print(f"Sum of blue pixels: {green_sum}")