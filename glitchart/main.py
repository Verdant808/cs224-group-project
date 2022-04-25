from PIL import Image
from glitchart.interval_creator import CHOICES as interval_choices
from glitchart.sorter import sort_image, choices as sorting_choices
from datetime import datetime
import os

def get_glitched(image_path, sorting_func, interval_func, lower_threshold=0.25, upper_threshold=0.85, angle=0, output_name=None):
    # open image and add all info to dictionary
    args = {
        'image': Image.open(image_path),
        'lower_threshold': lower_threshold,
        'upper_threshold': upper_threshold,
        'angle': angle,
        'sorting_func': sorting_func,
        'interval_func': interval_func
    }

    # create output path if none is entered
    if output_name is None: 
        date = datetime.today()
        output_name = f'{date.hour}:{date.minute}:{date.second} {date.month}-{date.day}-{date.year}.png'
    elif not output_name.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        output_name = f'{output_name}.png'
    output_path = os.getcwd() + os.path.sep + 'datafiles' + os.path.sep + output_name

    # perform the pixelsorting and return the image and path
    return {'img':pixelsort(**args), 'img_path': output_path}


def pixelsort(image, lower_threshold, upper_threshold, angle, sorting_func, interval_func):
    # save copy of original picture, convert to RGBA values, and save pixel data
    original = image
    image = image.convert('RGBA').rotate(angle, expand=True)
    image_data = image.load()

    # get intervals
    intervals = interval_choices[interval_func](image, lower_threshold=lower_threshold,
        upper_threshold=upper_threshold)
    # sort the pixels in the intervals
    sorted_pixels = sort_image(image.size, image_data, intervals, sorting_choices[sorting_func.lower()])

    # comibine sorted pixels with the original image
    output_img = place_pixels(sorted_pixels, image_data, image.size)
    if angle != 0:
        output_img = output_img.rotate(-angle, expand=True)
        output_img = crop_to(output_img, original)

    return output_img

# used to combine sorted with non-sorted pixels
def place_pixels(pixels, original, size):
    output_img = Image.new('RGBA', size)
    # for each column of pixels
    for y in range(size[1]):
        count = 0
        # get each individual pixel, row by row
        for x in range(size[0]):
            # place pixel if row was sorted
            output_img.putpixel((x, y), pixels[y][count])
            count += 1
    return output_img

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