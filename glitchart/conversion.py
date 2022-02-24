from colorsys import rgb_to_hsv

# convert pixel to hsv values and return lightness
def lightness(pixel): 
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0

# used to crop the sorted image to fit the original image
def crop_to(image_to_crop, reference_image):
    reference_size = reference_image.size
    current_size = image_to_crop.size
    dx = current_size[0] - reference_size[0]
    dy = current_size[1] - reference_size[1]
    left = dx / 2
    upper = dy / 2
    right = dx / 2 + reference_size[0]
    lower = dy / 2 + reference_size[1]
    return image_to_crop.crop(
        box=(
            int(left),
            int(upper),
            int(right),
            int(lower)))