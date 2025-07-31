import argparse
import logging

from sort import sort


def positive_float(value):
    try:
        f = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid quantity.")

    if f <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be >0.")
    return f

def parse_arguments():
    parser = argparse.ArgumentParser(description='Select stack for packages.')
    parser.add_argument('-w', '--width', dest='width', required=True, type=positive_float,
                        help='Width (cm)')
    parser.add_argument('-e', '--height', dest='height', required=True, type=positive_float,
                        help='Height (cm)')
    parser.add_argument('-l', '--lenght', dest='lenght', required=True, type=positive_float,
                        help='Lenght (cm)')
    parser.add_argument('-m', '--mass', dest='mass', required=True, type=positive_float,
                        help='Mass (cm)')
    return parser.parse_args()

def main():
    logging.basicConfig(
        format='%(asctime)s\t[%(name)s]\t[%(levelname)s]\t%(message)s', 
        datefmt="%Y-%m-%d %H:%M:%S%z",
        level=logging.INFO, encoding='utf-8',
        handlers=[
            logging.FileHandler('logs.log', 'a', 'utf-8'),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger(main.__qualname__)

    args: argparse.Namespace = parse_arguments()
    logger.info('%-18s %s', 'Width:', args.width)
    logger.info('%-18s %s', 'Height:', args.height)
    logger.info('%-18s %s', 'Lenght:', args.lenght)
    logger.info('%-18s %s', 'Mass:', args.mass)

    stack = sort(width=args.width,
         height=args.height,
         lenght=args.lenght,
         mass=args.mass)
    logger.info(f'Stack Selected: {stack}')


if __name__ == '__main__':
    main()