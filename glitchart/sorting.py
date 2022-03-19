from cmath import pi
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
    if pixel[0] <= pixel[1] & pixel[0] <= pixel[2]:
        return pixel[0]
    elif pixel[1] <= pixel[0] & pixel[1] <= pixel[2]:
        return pixel[1]
    elif pixel[2] <= pixel[0] & pixel[2] <= pixel[1]:
        return pixel[2]


#a vailable sorting function options
choices = {
    'lightness': lightness,
    'hue': hue,
    'saturation': saturation,
    'intensity': intensity,
    'minimum': minimum
}