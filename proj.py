from PIL import Image, ImageFilter, ImageDraw

im1 = Image.open("ban.jpg")
draw = ImageDraw.Draw(im1)


n = 0

(width, height) = im1.size
for x in range(width):
    for y in range(height):
        draw.point((x, y), (255, 255, 255))
im1.save("ban2.jpg")

im2 = Image.open("ban2.jpg")
draw.ImageDraw.Draw(im2)

# for x in range(width):
     # for y in range(height):
        # print "Processing pixel (%d %d)" % (x, y)
        # (r, g, b) = im.getpixel((x, y))
        # if 150 <= r <= 255 and 0 <= g <= 40 and 0 <= b <= 70:
            # draw.point((x, y), (255, 0, 0))
        # else:
            # draw.point((x, y), (255, 255, 255))

# print n
# draw.ellipse([(120, 120), (130, 130)], (255, 0, 0))

# im = im.filter(ImageFilter.GaussianBlur(3))
# draw.ellipse([(150, 150), (160, 160)], (255, 0, 0))


