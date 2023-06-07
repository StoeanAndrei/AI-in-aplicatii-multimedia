# Biblioteci utilizate
import cv2
import numpy as np

# Citirea imaginii
img = cv2.imread("D:\\Tema1AM\\Stoean_Andrei_332AB\\violet_train1.png")
# Aflarea dimensiunilor
img_height, img_width, img_channels = img.shape
#cv2.imshow("A violet train", img)
#cv2.waitKey(0)
#cv2.destroyWindow("A vioelt train")

# Citirea din fisier a coordonatelor in adnotare Darknet
with open("D:\\Tema1AM\\Stoean_Andrei_332AB\\yolov5-master\\runs\\detect\\exp\\labels\\violet_train1.txt", "r") as file:
    line = file.readline()
    values_str = line.split()
    values = [float(value) for value in values_str]

x, y, w, h = values[1], values[2], values[3], values[4]

# Transformarea coordonatelor in pixeli
x = int(x * img_width)
y = int(y * img_height)
w = int(w * img_width)
h = int(h * img_height)

# Aflarea coordonatelor in pixeli pentru coltul stanga-sus
x1 = int(x - w/2)
y1 = int(y - h/2)
# Aflarea coordonatelor in pixeli pentru coltul dreapta-jos
x2 = int(x + w/2)
y2 = int(y + h/2)

# Decuparea imaginii
crop = img[y1:y2, x1:x2]

# Salvarea imaginii decupate
cv2.imwrite("D:\\Tema1AM\\Stoean_Andrei_332AB\\violet_train1_crop.png", crop)
#cv2.imshow("Crop", crop)
#cv2.waitKey(0)
#cv2.destroyWindow("Crop")

# Conversia la spatiul de culoare CIE XYZ
img_xyz = cv2.cvtColor(crop, cv2.COLOR_BGR2XYZ)

# Salvarea imaginii in spatiul de culoare CIE XYZ
cv2.imwrite("D:\\Tema1AM\\Stoean_Andrei_332AB\\violet_train1_XYZ.png", img_xyz)
#img_crop = cv2.imread("violet_train1_XYZ.png")
#cv2.imshow("CIE XYZ", img_xyz)
#cv2.waitKey(0)
#cv2.destroyWindow("CIE XYZ")

# Definirea unui interval de culoare pentru violet
lower_violet = np.array([90, 40, 140])
upper_violet = np.array([160, 120, 200])

# Selectarea pixelilor din intervalul setat
mask = cv2.inRange(img_xyz, lower_violet, upper_violet)

# Aplicarea mastii pe imagine
result = cv2.bitwise_and(img_xyz, img_xyz, mask=mask)

# Conversia la spatiul original de culoare
result_mask = cv2.cvtColor(result, cv2.COLOR_XYZ2BGR)

# Salvarea imaginii dupa aplicarea mastii
cv2.imwrite("D:\\Tema1AM\\Stoean_Andrei_332AB\\violet_train1_mask.png", result_mask)
# Afisare imaginii dupa aplicarea mastii
#cv2.imshow("Rezultatul mastii", result_mask)
#cv2.waitKey(0)
#cv2.destroyAllWindows("Rezultatul mastii")

# Conversia la spatiul de culoare CIE XYZ
img_mask_xyz = cv2.cvtColor(result_mask, cv2.COLOR_BGR2XYZ)

# Salvarea imaginii in spatiul de culoare CIE XYZ
cv2.imwrite("D:\\Tema1AM\\Stoean_Andrei_332AB\\violet_train1_mask_XYZ.png", img_mask_xyz)
#img_crop = cv2.imread("violet_train1_mask_XYZ.png")
#cv2.imshow("Mask CIE XYZ", img_xyz)
#cv2.waitKey(0)
#cv2.destroyWindow("Mask CIE XYZ")
  
# Conversia imaginii in spatiul gri
tmp = cv2.cvtColor(result_mask, cv2.COLOR_BGR2GRAY)
  
# Aplicarea tehnicii tresholding
_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
  
# Impartirea imaginii dupa canalele de culoare
b, g, r = cv2.split(result_mask)
  
# Crearea unei liste reprezentand cele 4 canale 
rgba = [b, g, r, alpha]
  
# Imbinarea celor 4 canale intr-o imagine
img_transparency = cv2.merge(rgba, 4)
  
# Salvarea imaginii
cv2.imwrite("D:\\Tema1AM\\Stoean_Andrei_332AB\\violet_train1_transparency.png", img_transparency)
#cv2.imshow("Imagine cu transparenta", img_transparency)
#cv2.waitKey(0)
#cv2.destroyAllWindows("Imagine cu transparenta")