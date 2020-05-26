# stamp-signature-detection
Objective - To detect (localize &amp; classify) stamps and signatures in the scanned documents

This project uses tensorflow API fro object detection.

Process :
1. Dataset generation
2. models research and training
3. validation
4. output - bounding box generation


# STEPS TO FOLLOW:

Download TensorFlow Object Detection API repository from GitHub - (https://github.com/tensorflow/models)
or clone it - https://github.com/tensorflow/models.git

create these below named folders in models\research\object_detection folder :
1. images - containing folders named test and train that consists of test ana train image datasets along with their XML or TXT files.
2. inference_graph - it will be used lately to store the output inference graphs.
3. training - used to store the labelmap and .config files of the selected models , and checkpoints during training will also be saved here.

#### STEPS:

step1 - generate the csv files according to the test and train datasets - (xml_to_csv.py)

step2 - generate tfrecords for both - (generate_tfrecords.py)

step3 - create labelmap according to your custom data

step4 - select a model from the tensorflow model zoo ( https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md )

step5 - config the model (training folder)

step6 - train the model - ( model_main.py)

step7 - export the output inference graph

step8 - evaluate the model( mAP scores and confusion matrix)

step9 - run the inference script ( Object_detection_image.py) to get the output images with bounding boxes.
