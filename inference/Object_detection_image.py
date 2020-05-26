# print("shreya")

import os
import pathlib
import cv2
import numpy as np
import warnings
# import glob
warnings.filterwarnings("ignore")
import tensorflow as tf
import sys
# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util
import pandas as pd
# print("shreya")



df_count = pd.DataFrame(columns=['filename','stamp','signature'])
# Name of the directory containing the object detection module we're using
MODEL_NAME = 'inference_graph'

PATH_TO_TEST_IMAGES_DIR = pathlib.Path(os.path.join(os.getcwd(),'images/test/'))
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.png")))

# IMAGE_NAME = 'im1.png'
# Grab path to current working directory
CWD_PATH = os.getcwd()
# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

# Number of classes the object detector can identify
NUM_CLASSES = 2

for imagename in TEST_IMAGE_PATHS:
    # Path to image
    PATH_TO_IMAGE = os.path.join(PATH_TO_TEST_IMAGES_DIR,imagename) 
    print(PATH_TO_IMAGE)
    # Load the label map.
    # Label maps map indices to category names, so that when our convolution
    # network predicts `1`, we know that this corresponds to `stamp`.
    # Here we use internal utility functions, but anything that returns a
    # dictionary mapping integers to appropriate string labels would be fine
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    # Load the Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)
    # Define input and output tensors (i.e. data) for the object detection classifier
    # Input tensor is the image
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    # Output tensors are the detection boxes, scores, and classes
    # Each box represents a part of the image where a particular object was detected
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    # Each score represents level of confidence for each of the objects.
    # The score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
    # Number of objects detected
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')
    # Load image using OpenCV and
    # expand image dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
    image = cv2.imread(PATH_TO_IMAGE)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)
    # Perform the actual detection by running the model with the image as input
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})
    # Draw the results of the detection (aka 'visulaize the results')

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
    # All the results have been drawn on image. Now display the image.
    # print("shreya")
    # print(np.squeeze(classes))
    # print("boxes")
    # print(np.squeeze(scores))

    classes_out = (np.squeeze(classes))[np.where(np.squeeze(scores)>=score_thresh)[0]]
    print(classes_out)

    stamp_count = len(np.where(classes_out==1)[0])
    sign_count = len(classes_out)-stamp_count
    file_name = PATH_TO_IMAGE[PATH_TO_IMAGE.find('test')+5:]
    df_count = df_count.append({"filename":file_name,"stamp":stamp_count,"signature":sign_count},ignore_index=True)
    df_count.to_csv('object_counts.csv')

    imS = cv2.resize(image, (350,550))
    # cv2.imshow('Object detector', imS)
    # cv2.imshow("output", imS)
    # Press any key to close the image
    # cv2.waitKey(0)
    # Clean up
    cv2.destroyAllWindows()
