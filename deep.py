import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
import inception
from PIL import Image

# 1. CLONE: https://github.com/Hvass-Labs/TensorFlow-Tutorials.git

# 2. DOWNLOAD INCEPTION MODEL:
inception.data_dir = "pre_proc/training_data/"
#inception.maybe_download()

# 3. LOAD INCEPTION MODEL
model = inception.Inception()

# This is a simple wrapper-function for displaying the image,
# then classifying it using the Inception model and finally printing the classification scores.
def classify(image_path):
    # Display the image.
    #display(Image(image_path))
    Image.open(image_path).show()

    # Use the Inception model to classify the image.
    pred = model.classify(image_path=image_path)

    # Print the scores and names for the top-10 predictions.
    model.print_scores(pred=pred, k=10, only_first_name=True)

def plot_resized_image(image_path):
    # Get the resized image from the Inception model.
    resized_image = model.get_resized_image(image_path=image_path)

    Image.open(image_path).show()


image_path = os.path.join(inception.data_dir, '_-20_10_0.jpg')
classify(image_path)


model.close()

