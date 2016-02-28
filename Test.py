from PIL import Image, ImageFilter, ImageDraw

im = Image.open("ban.jpg")
draw = ImageDraw.Draw(im)

(width, height) = im.size
for x in range(width):
    for y in range(height):
        print "Processing pixel (%d %d)" % (x, y)
        (r, g, b) = im.getpixel((x, y))
        if 150 <= r <= 255 and 0 <= g <= 40 and 0 <= b <= 70:
            Draw.ellipse((5, 5), [5, 5], fill=None, outline=None)
            #draw.point((x, y), fill=(255, 255, 255))


#im = im.filter(ImageFilter.GaussianBlur(8))


im.save("ban1.jpg")

