import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images = []
    labels = []

    # Validate data_dir
    if not os.path.isdir(data_dir):
        raise ValueError(f"data_dir not found or not a directory: {data_dir}")

    for category in range(NUM_CATEGORIES):
        category_dir = os.path.join(data_dir, str(category))
        if not os.path.isdir(category_dir):
            # skip missing category directories (or raise if you prefer)
            continue

        for fname in os.listdir(category_dir):
            # Build full path in a platform-independent way
            file_path = os.path.join(category_dir, fname)

            # Skip directories and hidden files
            if not os.path.isfile(file_path) or fname.startswith('.'):
                continue

            # Read image (BGR by OpenCV)
            img = cv2.imread(file_path, cv2.IMREAD_COLOR)
            if img is None:
                # unreadable file (not an image or corrupted) — skip it
                continue

            # Resize to (width, height) for OpenCV
            img_resized = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))

            # Convert BGR to RGB (typical for ML pipelines)
            try:
                img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
            except Exception:
                # If conversion fails for some reason, fall back to resized BGR
                img_rgb = img_resized

            images.append(img_rgb)
            labels.append(category)

    return images, labels


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    input_shape = (IMG_WIDTH, IMG_HEIGHT, 3)

    model = tf.keras.models.Sequential([tf.keras.layers.InputLayer(input_shape = input_shape)])

    tf.keras.layers.Conv2D






if __name__ == "__main__":
    main()
