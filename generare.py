# Biblioteci
import time
import keras_cv
from tensorflow import keras
keras.mixed_precision.set_global_policy("float32")
import matplotlib.pyplot as plt
import cv2
from numba import jit, cuda
import numpy as np

#@jit(target_backend='cuda')

# Crearea modelului
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512, jit_compile=True)

# Crearea imaginilor din text
images = model.text_to_image("high quality realistic image of a violet train on the road", batch_size=3)

#def plot_images(images):
    # Set figure size
    #plt.figure(figsize=(20, 20))
    # Loop through each image
    #for i in range(len(images)):
        # Subplot setup
        #ax = plt.subplot(1, len(images), i+1)
        # Plot each image
        #plt.imshow(images[i])
        # Do not show axis
        #plt.axis("off")

# Plotarea imaginilor prin apelarea functiei
#plot_images(images)

# Salvarea imaginilor
status1 = cv2.imwrite("violet_train1.png", images[0])
status2 = cv2.imwrite("violet_train2.png", images[1])
status3 = cv2.imwrite("violet_train3.png", images[2])