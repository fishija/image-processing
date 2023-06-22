from PIL import Image

def toBlackAndWhite(ogImage):
    return ogImage.convert('L')

def toSepia(ogImage, W):
    imgHeight, imgWidth = ogImage.size

    #greyscale image
    bwImage = toBlackAndWhite(img_original)
    bwImage.save('SP_greyscale.jpg')

    pixelsBW = bwImage.load()
    pixelsOG = ogImage.load()

    for i in range(imgHeight):
        for j in range(imgWidth):
            pxColor = pixelsBW[i,j]

            r = pxColor
            g = pxColor
            b = pxColor

            r = r + (W *2)
            g = g + W
            b = b

            if r>255:
                r = 255
            if g>255:
                g=255

            pixelsOG[i, j] = (r, g, b)

    return ogImage

if __name__ == '__main__':
    # W - zadany współczynnik wypełnienia barwą (od 20 do 40)
    W = 30
    
    #normal colors image
    img_original = Image.open('SP_og.jpg')

    #sepia image
    img_sepia = toSepia(img_original, W)

    #save images
    img_sepia.save('SP_sepia.jpg')
    