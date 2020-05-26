from PIL import Image
import os, sys
from tqdm import tqdm

path = #path of dir
dirs = os.listdir( path )

def resize():
    for item in tqdm(dirs):
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((360,504), Image.ANTIALIAS)
            imResize.save(f + ' resized.png', 'PNG', quality=90)

resize()
