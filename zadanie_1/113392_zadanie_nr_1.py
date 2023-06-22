from PIL import Image
import numpy as np
import math

def bilinearInterpolation(imgOg, new_w, new_h):

	old_h, old_w, c = imgOg.shape

	resized = np.zeros((new_h, new_w, c))

	w_scale = 0
	h_scale = 0

	if new_w != 0:
		w_scale = old_w / new_w

	if new_h != 0:
		h_scale = old_h / new_h
		
	for i in range(new_h):
		for j in range(new_w):
			x = i * h_scale
			y = j * w_scale
			
			x_floor = math.floor(x)
			x_ceil = min( old_h - 1, math.ceil(x))
			y_floor = math.floor(y)
			y_ceil = min(old_w - 1, math.ceil(y))

			if (x_ceil == x_floor) and (y_ceil == y_floor):
				q = imgOg[int(x), int(y), :]
			elif (x_ceil == x_floor):
				q1 = imgOg[int(x), int(y_floor), :]
				q2 = imgOg[int(x), int(y_ceil), :]
				q = q1 * (y_ceil - y) + q2 * (y - y_floor)
			elif (y_ceil == y_floor):
				q1 = imgOg[int(x_floor), int(y), :]
				q2 = imgOg[int(x_ceil), int(y), :]
				q = (q1 * (x_ceil - x)) + (q2	 * (x - x_floor))
			else:
				v1 = imgOg[x_floor, y_floor, :]
				v2 = imgOg[x_ceil, y_floor, :]
				v3 = imgOg[x_floor, y_ceil, :]
				v4 = imgOg[x_ceil, y_ceil, :]

				q1 = v1 * (x_ceil - x) + v2 * (x - x_floor)
				q2 = v3 * (x_ceil - x) + v4 * (x - x_floor)
				q = q1 * (y_ceil - y) + q2 * (y - y_floor)

			resized[i,j,:] = q

	return resized.astype(np.uint8)

if __name__ == '__main__':
    
    #image dimensions before: 1024 x 778
    img_original = Image.open('SP_og.jpg')

    img_resized = Image.fromarray(bilinearInterpolation(np.asarray(img_original), 2048, 1556))

    #image dimensions after: 512 x 384 
    img_resized.save('SP_resized.jpg')
    