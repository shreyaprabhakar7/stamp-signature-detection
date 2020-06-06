from PIL import Image
import os, shutil
from os import listdir,makedirs
from os.path import isfile,join
from tqdm import tqdm

directory = r'OpenLabeling-master-main/main/300_resized/'

for filename in tqdm(os.listdir(directory)):
    if filename.endswith(".tif"):
        im = Image.open(join(directory,filename))
        name = join(directory,filename[:-4])
        im.save(name + '.png')
        print(os.path.join(directory, filename))
        continue
    else:
        continue