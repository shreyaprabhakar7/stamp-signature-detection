import os
from pdf2image import convert_from_path
from tqdm import tqdm

# pdf_dir = r"/content/gdrive/My Drive/TensorFlow/models/research/object_detection/pdf_test"
os.chdir(pdf_dir)

for pdf_file in tqdm(os.listdir(pdf_dir)):

    if pdf_file.endswith(".pdf"):

        pages = convert_from_path(pdf_file, 300)
        pdf_file = pdf_file[:-4]

    for page in pages:

        page.save("%s-page%d.png" % (pdf_file,pages.index(page)), "PNG")