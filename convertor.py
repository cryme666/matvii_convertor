from PIL import Image
import pandas as pd
from fpdf import FPDF
import os

FOLDER = './files/'

def get_new_path(file_name):
    return FOLDER + file_name

# png -> jpg
def png_to_jpg(png_file_path):
    img = Image.open(png_file_path)

    jpg_file_name = png_file_path.split(FOLDER)[1].split('.')[0] + '.jpg'
    
    jpg_img = img.convert('RGB')

    new_path = get_new_path(jpg_file_name)

    jpg_img.save(new_path)

    return new_path

# jpg -> png
def jpg_to_png(jpg_file_path):
    img = Image.open(jpg_file_path)

    png_file_name = jpg_file_path.split(FOLDER)[1].split('.')[0] + '.png'
    
    png_img = img.convert('RGBA')

    new_path = get_new_path(png_file_name)

    png_img.save(new_path)

    return new_path


# txt -> pdf

# xlsx -> csv
def xlsx_to__csv(xlsx_file_path):
    df = pd.read_excel(xlsx_file_path)


    csv_file_name = xlsx_file_path.split(FOLDER)[1].split('.')[0] + '.csv'
    new_path = get_new_path(csv_file_name)

    df.to_csv(new_path)
    return new_path



# csv -> xlsx

if __name__ == '__main__':
    jpg_to_png(FOLDER + 'image.jpg')