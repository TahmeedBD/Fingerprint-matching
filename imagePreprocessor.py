import numpy as np
import os
import cv2


image_directory = 'images'
output_directory = 'images/output'

allowed_extensions = ['.bmp', '.jpg', '.jpeg', '.png']

image_files = [file for file in os.listdir(
    image_directory) if os.path.splitext(file)[1] in allowed_extensions]

images = []


def preprocess_image(image):

    img = cv2.imread(image)

    # TODO Add image preprocessing here

    return img


for file in image_files:
    images.append(preprocess_image(os.path.join(image_directory, file)))

for i, image in enumerate(images):
    cv2.imwrite(os.path.join(output_directory,
                f'output__{image_files[i]}'), image)
