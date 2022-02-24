from colorsys import rgb_to_hsv

# converts a pixel color to lightness value
def lightness(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0


#available sorting function options
choices = {
    "lightness": lightness
}