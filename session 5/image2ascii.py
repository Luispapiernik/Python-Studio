from argparse import ArgumentParser
from PIL import Image


def convert_to_ascii(image_name):
    python_logo = Image.open(image_name)
    python_logo = python_logo.convert("L")

    python_logo.show()

    long_ascii_palette = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def main():
    # definir los parametros
    parser = ArgumentParser()

    parser.add_argument("-in", "--image-name", type=str, help="Name of the image to convert")

    args = parser.parse_args()
    convert_to_ascii(args.image_name)

main()
