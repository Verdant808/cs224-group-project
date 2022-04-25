
from colorsys import rgb_to_hsv

# converts a pixel color to lightness value
def lightness(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0


# converts a pixel color to hue value
def hue(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[0] / 255.0


# converts a pixel color to saturation value
def saturation(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[1] / 255.0


# converts a pixel color to its intensity value
def intensity(pixel):
    return (pixel[0] + pixel[1] + pixel[2]) / 3


# gets the lesser value of the RGB representation
def minimum(pixel):
    return min(pixel)


# a vailable sorting function options
choices = {
    'lightness': lightness,
    'hue': hue,
    'saturation': saturation,
    'intensity': intensity,
    'minimum': minimum
}

# used to sort pixels in intervals
def sort_image(size, image_data, intervals, sorting_func):
    sorted_pixels = []
    # for each column of pixels
    for y in range(size[1]):
        row = []
        x_min = 0
        # get each individual pixel, row by row
        for x_max in intervals[y] + [size[0]]:
            interval = []
            # add each pixel from an interval to a list
            for x in range(x_min, x_max):
                interval.append(image_data[x, y])
            # sort intervals
            row += sort_interval(interval, sorting_func)
            x_min = x_max
        sorted_pixels.append(row)
    return sorted_pixels


# used to sort intervals of pixels, based on entered function
def sort_interval(interval, sorting_func):
    return [] if interval == [] else sorted(interval, key=sorting_func)