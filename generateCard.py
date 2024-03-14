from PIL import Image
from tkinter import PhotoImage, Label, Tk
# for generating the card images from a single image named card.jpg

# Open the image file
img = Image.open('img/card.jpg')

# Size of each card
card_width = 85
card_height = 99

# Loop over the image
for i in range(4):
    for j in range(13):
        # Calculate the position of each card
        left = j * card_width
        upper = i * card_height
        right = left + card_width
        lower = upper + card_height

        # Crop each card
        card_img = img.crop((left, upper, right, lower))

        # Save each card as a separate file
        card_img.save(f'img/card_{i}_{j+2}.png')