"""
Module with tools to produce the final input for files.
"""

import cv2
from converter import convert_image


def image_to_ascii(image_path2):

    try: 

        image = cv2.imread(image_path)
    
    except:

        raise Exception("No valid path for image entered.")

    ascii_image = convert_image(image)

    return ascii_image
    
def video_to_ascii()
    
    return video 

def to_ascii(file, mode : str)

    """
mode : video or image.
    """

    if mode == "video":

        video_to_ascii()

    elif mode == "image":

        image_to_ascii()

    else:

        raise Exception("Mode not supported!")

    return result

