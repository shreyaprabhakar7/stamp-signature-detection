
import os
import pathlib
import cv2
import numpy as np
import warnings
import matplotlib.pyplot as plt
# %matplotlib inline

from pdf2image import convert_from_path
from tqdm import tqdm

# import glob

warnings.filterwarnings("ignore")
import tensorflow as tf
import sys

from PIL import Image
import shutil
from os import listdir,makedirs
from os.path import isfile,join


# # This is needed since the notebook is stored in the object_detection folder.



pdf_dir = r"/content/gdrive/My Drive/tensorflow2/models/research/object_detection/images/test"
pdf_dir = os.path.join(os.getcwd(), "./images/test")
os.chdir(pdf_dir)

for pdf_file in tqdm(os.listdir(pdf_dir)):

    if pdf_file.endswith(".pdf"):
        pages = convert_from_path(pdf_file, 300)
        pdf_file = pdf_file[:-4]
        
        for page in pages:

            page.save("%s-page%d.png" % (pdf_file,pages.index(page)), "PNG")

  


directory = os.path.join(os.getcwd(), "./images/test")

for filename in tqdm(os.listdir(directory)):
    if filename.endswith(".jpg"):
        im = Image.open(join(directory,filename))
        name = join(directory,filename[:-4])
        im.save(name + '.png')
        print(os.path.join(directory, filename))
        continue
    else:
        continue
    

directory = os.path.join(os.getcwd(), "./images/test")

for filename in tqdm(os.listdir(directory)):
    if filename.endswith(".tif"):
        im = Image.open(join(directory,filename))
        name = join(directory,filename[:-4])
        im.save(name + '.png')
        print(os.path.join(directory, filename))
        continue
    else:
        continue
    
    
    
    

dir = os.getcwd()
os. chdir(dir)

sys.path.append("..")

from utils import label_map_util
from utils import visualization_utils as vis_util
import pandas as pd

df_count = pd.DataFrame(columns=['filename','stamp','signature'])
df_cord = pd.DataFrame(columns=['filename','class','xmin','ymin','xmax','ymax'])
# # Name of the directory containing the object detection module we're using
MODEL_NAME = 'inference_graph'

PATH_TO_TEST_IMAGES_DIR = pathlib.Path(os.path.join(os.getcwd(),'images/test/'))
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.png")))

CWD_PATH = os.getcwd()

print(CWD_PATH)
# # Path to frozen detection graph .pb file, which contains the model that is used
# # for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
print(PATH_TO_CKPT)
# # Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')
print(PATH_TO_LABELS)

# # Number of classes the object detector can identify
NUM_CLASSES = 2

for imagename in TEST_IMAGE_PATHS:
#     # Path to image
    PATH_TO_IMAGE = os.path.join(PATH_TO_TEST_IMAGES_DIR,imagename) 
#     print(PATH_TO_IMAGE)
#     # Load the label map.
#     # Label maps map indices to category names, so that when our convolution
#     # network predicts `1`, we know that this corresponds to `stamp`.
#     # Here we use internal utility functions, but anything that returns a
#     # dictionary mapping integers to appropriate string labels would be fine
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
#     # Load the Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)
#     # Input tensor is the image
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
#     # Output tensors are the detection boxes, scores, and classes
#     # Each box represents a part of the image where a particular object was detected
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
#     # Each score represents level of confidence for each of the objects.
#     # The score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
#     # Number of objects detected
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    image = cv2.imread(PATH_TO_IMAGE)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)
#     # Perform the actual detection by running the model with the image as input
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})
#     # Draw the results of the detection (aka 'visulaize the results')

    score_thresh=0.50
    vis_util.visualize_boxes_and_labels_on_image_array(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=score_thresh)
    
#     print(boxes[0])
    
#     print(np.squeeze(boxes))
    
    height,width,_ = image.shape
    mask_score = np.where(np.squeeze(scores)>score_thresh)[0]
    detected_boxes = np.squeeze(boxes)[mask_score,:]
    detected_class = np.squeeze(classes)[mask_score]
    
    for i, b in enumerate(detected_boxes):        
#         print(width,height)
        label_dect = detected_class[i]
        ymin = b[0]*height
        xmin = b[1]*width
        ymax = b[2]*height
        xmax = b[3]*width
        
        # print("label="+str(int(label_dect))+"  Dims="+str([ymin,xmin,ymax,xmax]))
        
        file_name = PATH_TO_IMAGE[PATH_TO_IMAGE.find('test')+5:]
        if str(int(label_dect)) == '2':
            class_set = "signature"
             
        else:
            class_set = "stamp"
            
        
        df_cord = df_cord.append({"filename":file_name,"class":class_set,"xmin":xmin,"ymin":ymin,"xmax":xmax,"ymax":ymax},ignore_index=True)
        df_cord.to_csv('object_cords.csv')
        
        
         
        
    # width,height=image.size
    
    # print(np.squeeze(boxes))
    # boxes = np.squeeze(boxes)
    # print(boxes)
    # print(height)

     # for i,b in enumerate(boxes[0]):
     #    width = boxes[0][i][1]+boxes[0][i][3]
     #    height = boxes[0][i][0]+boxes[0][i][2]
        
     #    print(width, height)
     #    print(height)


    classes_out = (np.squeeze(classes))[np.where(np.squeeze(scores)>=score_thresh)[0]]
    # print(classes_out)

    stamp_count = len(np.where(classes_out==1)[0])
    sign_count = len(classes_out)-stamp_count
    file_name = PATH_TO_IMAGE[PATH_TO_IMAGE.find('test')+5:]
    df_count = df_count.append({"filename":file_name,"stamp":stamp_count,"signature":sign_count},ignore_index=True)
    df_count.to_csv('object_counts.csv')

    imS = cv2.resize(image, (350,550))
    print(imS)
#     # cv2.imshow('Object detector', imS)
    # cv2.imshow("output", imS)
#     # Press any key to close the image
    # cv2.waitKey(0)
# #     # Clean up
    # cv2.destroyAllWindows()
