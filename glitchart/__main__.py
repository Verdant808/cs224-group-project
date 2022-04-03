from PIL import Image
from glitchart.command_line_args import get_args
from glitchart.main import pixelsort
from datetime import datetime

# args = get_args()

def get_args(image_path, output_name, lower_threshold, upper_threshold, angle, sorting_func, interval_func):
    args = {}

    # open image and add to dictionary
    args['image'] = Image.open(image_path)

    # pop output path and create if none was entered
    output_path = args.pop('output_name')
    if output_path is None: 
        output_path = 'glitched_out.png'

    # perform the pixelsorting and save image to pathname
    pixelsort(**args).save(output_path)
