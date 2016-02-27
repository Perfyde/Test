from PIL import Image, ImageFilter

im = Image.open("WPP.jpg")

im1 = im.filter(ImageFilter.GaussianBlur(8))

# write to stdout
im1.save("WPP4.jpg")
