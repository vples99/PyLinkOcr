import io
import pytesseract
import argparse

# Add argument parsing further down, it should work for clipboard images by default but be able to access an image
# using a path as an argument

def grab_img():
    pass
    #TODO

def pre_process_img():
    pass
    #TODO

def process_img():
    #TODO
    pass

def extract():
    #TODO
    pass

parser = argparse.ArgumentParser(description="Optical character recognition for links in images")
parser.add_argument('src', type=str, help='Source image as a path')
args = parser.parse_args()
print(args.src)
# TODO Must check if the argument returns a valid directory / image


