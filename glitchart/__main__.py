from PIL import Image
from glitchart.main import pixelsort
from datetime import datetime

def get_args(image_path, output_name, lower_threshold, upper_threshold, angle, sorting_func, interval_func):
    # open image and add all info to dictionary
    args = {
        'image': Image.open(image_path),
        'output_name': output_name,
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

    # perform the pixelsorting and save image to pathname
    pixelsort(**args).save(output_name)