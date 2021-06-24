"""
Module, containning the tools to proccess the image.
"""

import cv2
import os


ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']


def resize_image(image, new_width=25):

    (input__width, input__height) = image.shape[:2]
    aspect_ratio = input__height/float(input__width)

    changed_height = int(aspect_ratio * new_width)

    changed_image = cv2.resize(image, (new_width, changed_height))

    return changed_image

def make_grey(image):
    
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def pixel_to_ascii(image, range_width=25):

    pixels_in_image = list(image.ravel())
    pixels_to_chars = [ASCII_CHARS[pixel_value//range_width] for pixel_value in pixels_in_image]

    return "".join(pixels_to_chars)

def image_to_ascii(image, new_width=25):
    
    image = resize_image(image)
    image = make_grey(image)
    
    pixels_to_chars = pixel_to_ascii(image)
    len_pixels_to_chars = len(pixels_to_chars)
    
    image_ascii = [pixels_to_chars[index: index + new_width] for index in range(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def convert_image(image):
    
    image_ascii = image_to_ascii(image)
    
    return image_ascii
