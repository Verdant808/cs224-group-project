
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