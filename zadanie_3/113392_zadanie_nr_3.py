import cv2 as cv
import numpy as np


def gauss_3x3(img):
    blr = cv.GaussianBlur(img, (3,3), 0)
    sharpened = 2. * img - blr
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)

    return sharpened


def gauss_15x15(img):
    blr = cv.GaussianBlur(img, (15,15), 0)
    sharpened = 2. * img - blr
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)

    return sharpened


def img_erosion(img, kernel):
    img_erosion = cv.erode(img, kernel, iterations=1)
    return img_erosion


def img_dilation(img, kernel):
    img_dilation = cv.dilate(img, kernel, iterations=1)
    return img_dilation


def img_opening(img, kernel):
    img_open = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    return img_open


def img_closing(img, kernel):
    img_close = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    return img_close


if __name__ == '__main__':

    img_original = cv.imread('SP.jpg')
    kernel = np.ones((5,5), np.uint8)


    # image sharpening

    img = gauss_3x3(img_original)
    cv.imwrite('SP_sharp_3x3.jpg', img)

    img = gauss_15x15(img_original)
    cv.imwrite('SP_sharp_15x15.jpg', img)


    # image erosion and dialation

    img = img_erosion(img_original, kernel)
    cv.imwrite('SP_erosion.jpg', img)

    img = img_dilation(img_original, kernel)
    cv.imwrite('SP_dilation.jpg', img)


    # image opening and closing

    img = img_opening(img_original, kernel)
    cv.imwrite('SP_open.jpg', img)

    img = img_closing(img_original, kernel)
    cv.imwrite('SP_close.jpg', img)
