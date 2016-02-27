from PIL import Image, ImageFilter

im = Image.open("poisson.jpg")

(width, height) = im.size
for x in range(width):
    for y in range(height):
        print "Processing pixel (%d %d)" % (x, y)
        (r, g, b) = im.getpixel((x, y))
        if 150 <= r <= 255 and 0 <= g <= 40 and 0 <= b <= 70:
            im.putpixel((x, y), (255, 0, 0))
        else:
            im.putpixel((x, y), (255, 255, 255))

im = im.filter(ImageFilter.GaussianBlur(8))

# write to stdout
im.save("poisson1.jpg")

