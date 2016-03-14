from PIL import Image, ImageFilter, ImageDraw

im = Image.open("ban.jpg")
draw = ImageDraw.Draw(im)

(width, height) = im.size
for x in range(width):
    for y in range(height):
        print "Processing pixel (%d %d)" % (x, y)
        (r, g, b) = im.getpixel((x, y))
        if 150 <= r <= 255 and 0 <= g <= 40 and 0 <= b <= 70:
            draw.ellipse([(x, y), (x+10, y+10)], (255, 0, 0))
        else:
            draw.point((x, y), fill=(255, 255, 255))



#im = im.filter(ImageFilter.GaussianBlur(3))
#draw.ellipse([(150, 150), (160, 160)], (255, 0, 0))

im.save("ban1.jpg")