from PIL import Image
from glitchart.conversion import lightness

# creates and returns a list of intervals for sorting, based on lightness
def threshold(image, lower_threshold, upper_threshold, **args):
    intervals = []
    image_data = image.load()

    # for each column of pixels
    for y in range(image.size[1]):
        intervals.append([])
        # get each individual pixel, row by row
        for x in range(image.size[0]):
            # add pixel to interval if lightness level is outside threshold
            level = lightness(image_data[x,y])
            if level < lower_threshold or level > upper_threshold:
                intervals[y].append(x)
    return intervals

CHOICES = {
    'threshold': threshold
}