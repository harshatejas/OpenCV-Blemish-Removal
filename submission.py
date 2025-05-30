import cv2
import numpy as np

def var_abs_laplacian(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)
    
    variance = laplacian.var()
    
    return variance

def mouse_handler(event, x, y, flags, data):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)

        x, y = center
        r1 = 10
        r2 = 50

        src = img[y - r1: y + r1, x - r1: x + r1]

        patches = {}

        patches[1] = img[y - r2: y - r1, x - r2: x - r1]
        patches[2] = img[y - r2: y - r1, x - r1: x + r1]
        patches[3] = img[y - r2: y - r1, x + r1: x + r2]
        patches[4] = img[y - r1: y + r1, x - r2: x - r1]
        patches[5] = img[y - r1: y + r1, x + r1: x + r2]
        patches[6] = img[y + r1: y + r2, x - r2: x - r1]
        patches[7] = img[y + r1: y + r2, x - r1: x + r1]
        patches[8] = img[y + r1: y + r2, x + r1: x + r2] 

        variance = []
        for key in patches.keys():
            if patches[key].size > 0:  # Ensure patch is not empty
                variance.append(var_abs_laplacian(patches[key]))
            else:
                variance.append(float('inf'))  # Assign high variance to invalid patches

        minimum_variance = min(variance)
        minimum_variance_index = variance.index(minimum_variance)

        if minimum_variance == float('inf'):
            print("Warning: No valid patches found at this location.")
            return

        final_patch = patches[minimum_variance_index + 1]

        mask = 255 * np.ones(src.shape, src.dtype)
        img = cv2.seamlessClone(final_patch, img, mask, center, cv2.NORMAL_CLONE)
        cv2.imshow(win_name, img)

img = cv2.imread("blemish.png")
if img is None:
    raise FileNotFoundError("Could not load 'blemish.png'. Ensure the file exists in the project directory.")

win_name = 'Blemish Remover'

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, mouse_handler)

# Wait for key press and save the final image
cv2.waitKey(0)
cv2.imwrite("output_blemish_removed.png", img)
cv2.destroyAllWindows()