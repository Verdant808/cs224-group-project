from PIL import Image
from glitchart.interval_creator import CHOICES as interval_choices
from glitchart.sorting import choices as sorting_choices
from glitchart.sorter import sort_image
from glitchart.conversion import crop_to

def pixelsort(image,
    lower_threshold,
    upper_threshold,
    angle,
    sorting_func, 
    interval_func
):
    # save copy of original picture, convert to RGBA values, and save pixel data
    original = image
    image = image.convert('RGBA').rotate(angle, expand=True)
    image_data = image.load()

    # get intervals
    intervals = interval_choices[interval_func](image, lower_threshold=lower_threshold,
        upper_threshold=upper_threshold)

    # sort the pixels in the intervals
    sorted_pixels = sort_image(image.size, image_data, intervals, sorting_choices[sorting_func])

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