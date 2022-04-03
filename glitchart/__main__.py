from time import ctime
from PIL import Image
from glitchart.command_line_args import get_args
from glitchart.main import pixelsort
from datetime import datetime

args = get_args()

# pop image path, open, and add to dictionary
image_path = args.pop('image')
args['image'] = Image.open(image_path)

# pop output path and create if none was entered
output_path = args.pop('output_name')
if output_path is None: 
    date = datetime.today()
    output_path = f'{date.hour}:{date.minute}:{date.second} {date.month}-{date.day}-{date.year}.png'

# perform the pixelsorting and save image to pathname
pixelsort(**args).save(output_path)