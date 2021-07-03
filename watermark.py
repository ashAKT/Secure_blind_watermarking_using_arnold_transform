from PIL import Image
from blind_watermark import WaterMark
import numpy as np
import time, sys

from numpy.lib.function_base import extract
from arnold import Arnold
import os

def main(argv):
    img_orgnl = input("original image: ")
    watermark_logo = input("watermark logo: ")
    
    scrambled_img = perform_arnold_transform(watermark_logo)
    embed_img = blind_watermark(img_orgnl,scrambled_img)
    extract_mrk = extract_watermark(embed_img)

    array_scram_img = np.array(Image.open(extract_mrk).convert("L"))
    resconstruct_img = inverse_arnold_transform(array_scram_img)

def perform_arnold_transform(watermark_logo):
    rounds = 33
    watermark = np.array(Image.open(watermark_logo).convert("L"))
    arnold = Arnold(rounds)
    scrambled = arnold.applyTransformTo(watermark)
    im = Image.fromarray(scrambled).convert("L")
    im.save("1scrambled.png", format="PNG")
    scrambled_img = os.path.basename("1scrambled.png")
    return scrambled_img

def blind_watermark(img_orgnl,scram_img):
    bwm1 = WaterMark(password_wm=1, password_img=1)
    # read original image
    bwm1.read_img(img_orgnl)
    # read watermark
    bwm1.read_wm(scram_img)
    #embed
    bwm1.embed('2embedded.png')
    embed_img = os.path.basename('2embedded.png')
    return embed_img

def extract_watermark(embed_img):
    bwm1 = WaterMark(password_wm=1, password_img=1)
    # notice that wm_shape is necessary
    bwm1.extract(filename=embed_img, wm_shape=(128, 128), out_wm_name='3extracted.png', )
    extract_mrk = os.path.basename('3extracted.png')
    return extract_mrk

def inverse_arnold_transform(array_scram_img):
    rounds = 40
    arnold = Arnold(rounds)
    reconstructed = arnold.applyInverseTransformTo(array_scram_img)
    im = Image.fromarray(reconstructed).convert("L")
    im.save("4reconstructed.png", format="PNG")

if __name__ == '__main__':
    main(sys.argv[1:])
