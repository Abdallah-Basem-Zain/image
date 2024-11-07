from tkinter import filedialog
import cv2
from PIL import Image
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label
from skimage.segmentation import watershed
from skimage.measure import regionprops
from skimage.color import label2rgb
from skimage import io, color, filters, measure, segmentation

footer = ""



def log_transform(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    c = 255 / np.log(1 + np.max(image))
    log_transformed = c * (np.log(image + 1+0.00000003))
    save_temp_images(1, "log", log_transformed)

def negative_transform(image_path):
    image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    neg = np.max(image)-image
    save_temp_images(1, "negative", neg)

def power_law_transform(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    power_law = 20 * np.power(image, .3)
    # power_law = ((power_law - power_law.min()) * (255 / (power_law.max() - power_law.min()))).astype(np.uint8)
    save_temp_images(1, "power", power_law)


def Thresholding(img_path , number):
    I = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    save_temp_images(1, "gray", I)
    level = cv2.threshold(I, number, 255, cv2.THRESH_BINARY)
    seg_I = np.zeros_like(I)
    seg_I[I > level[0]] = 255
    save_temp_images(0 , "thresholding" , seg_I)


def global_adaptive_thresholding(img_path , number1 , number2):
    # number1 :surrounding number of pixels that will have threshlding applied to it 11 (must be odd)
    # number2: is the mius from threshold
    I = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    level = cv2.adaptiveThreshold(I, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , number1 , number2)
    save_temp_images(0 , "adaptive_threshold" , level)

def save_temp_images(type, name, img):
    if type == 0:
        cv2.imwrite("seg/"+name+".png", img)
    else:
        cv2.imwrite("enhance/"+name+".png", img)



def watershed(image_path):
    image = io.imread(image_path)
    gray_image = color.rgb2gray(image)

    threshold_value = filters.threshold_otsu(gray_image)
    bw = gray_image > threshold_value

    # Compute distance transform
    D = np.zeros_like(bw, dtype=np.float64)
    D[bw] = 0
    D[~bw] = np.inf

    # Perform watershed segmentation
    markers, num_features = label(bw)
    L = segmentation.watershed(-D, markers, mask=bw)
    L[~bw] = 999
    save_temp_images(0, "wShed", L)
def get_path(file_path):
    global footer
    footer = file_path.split(".", -1)[1]
    return file_path


def save_picture(file_path):
    img = Image.open(file_path)
    print(footer)
    img.save("application-images/img.jpg")


def save_temp_images(type, name, img):
    if type == 0:
        cv2.imwrite("seg/"+name+".png", img)
    else:
        cv2.imwrite("enhance/"+name+".png", img)


def save_output(image):
    root = tk.Tk()
    root.withdraw()
    output_path = filedialog.asksaveasfilename(
        initialdir="/",
        title="Save Log-Transformed Image",
        filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")],
        defaultextension=".jpg"
    )

    if output_path:
        cv2.imwrite(output_path, image)
        print(f"Log-transformed image saved successfully at: {output_path}")
    else:
        print("Saving operation canceled.")


