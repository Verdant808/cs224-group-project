from PIL import Image
from glitchart.sorter import lightness
import random

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

# TODO: DOESN'T WORK YET
# creates an interval and adds all pixels to for sorting 
def none(image, **args):
    intervals = []
    image_data = image.load()

    # for each column of pixels
    for y in range(image.size[1]):
        intervals.append([])
        # get each individual pixel, row by row
        for x in range(image.size[0]):
            # add pixel to interval if lightness level is outside threshold
            level = lightness(image_data[x,y])
            if level < 0 or level > 1:
                intervals[y].append(x)
    return intervals

    # intervals = []

    # # for each column of pixels
    # for y in range(image.size[1]):
    #     intervals.append([])
    #     # get each individual pixel, row by row
    #     for x in range(image.size[0]):
    #         # add pixel to interval
    #         intervals[y].append(x)
    # return intervals


# creates an interval and adds pixels at random for sorting
def random_intervals(image, lower_threshold, upper_threshold, **args):
    intervals = []

    # for each column of pixels
    for y in range(image.size[1]):
        intervals.append([])
        # get each individual pixel, row by row
        for x in range(image.size[0]):
            # add pixel to interval at random
            rand = random.random()
            if rand < lower_threshold or rand > upper_threshold:
                intervals[y].append(x)
    return intervals


CHOICES = {
    'threshold': threshold,
    'none': none,
    'random': random_intervals
}