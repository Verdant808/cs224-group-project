import argparse
from glitchart.constant import DEFAULTS

def get_args():
    parser = argparse.ArgumentParser(description='argument reader')

    # get input image file name
    parser.add_argument('image')

    # get output image file name
    parser.add_argument('-o', '--output_name')

    # get lower threshold value
    parser.add_argument('-l', '--lower_threshold', type=float, default=DEFAULTS['lower_threshold'])

    # get upper threshold value
    parser.add_argument('-u', '--upper_threshold', type=float, default=DEFAULTS['upper_threshold'])

    # get angle used for sorting
    parser.add_argument('-a', '--angle', type=float, default=DEFAULTS['angle'])

    # get sorting function used to sort pixels
    parser.add_argument('-s', '--sorting_func', default=DEFAULTS['sorting_func'])

    # get interval function type used to create intervals 
    parser.add_argument('-i', '--interval_func', default=DEFAULTS['interval_func'])

    # Assign Namespace to make dictionary and return. The keys will be the name with the double flag("--")
    args = parser.parse_args()

    return {
        'image': args.image,
        'output_name': args.output_name,
        'lower_threshold': args.lower_threshold,
        'upper_threshold': args.upper_threshold,
        'angle': args.angle,
        'sorting_func': args.sorting_func,
        'interval_func': args.interval_func
    }