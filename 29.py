from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Tulip Example")

# Create a canvas
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Load the image
img = Image.open("tulip2.jpg")  # Use your image file here
img = ImageTk.PhotoImage(img)

# Add image to canvas
canvas.create_image(0, 0, anchor=NW, image=img)

root.mainloop()
