from PIL import Image, ImageFilter, ImageDraw

im1 = Image.open("ban.jpg")
draw = ImageDraw.Draw(im1)


n = 0

(width, height) = im1.size
im2 = Image.new("RGB", (width, height), (255, 255, 255))
im2.save("Bant.jpg")

d = ImageDraw.Draw(im2)

for x in range(width):
    for y in range(height):
        print "Processing pixel im2 (%d %d)" % (x, y)
        (r, g, b) = im1.getpixel((x, y))
        if 150 <= r <= 255 and 0 <= g <= 40 and 0 <= b <= 70:
            d.ellipse([(x, y), (x+10, y+10)], (255, 0, 0))
im2.save("ban2.jpg")




# print n
# draw.ellipse([(120, 120), (130, 130)], (255, 0, 0))

# im = im.filter(ImageFilter.GaussianBlur(3))
# draw.ellipse([(150, 150), (160, 160)], (255, 0, 0))


