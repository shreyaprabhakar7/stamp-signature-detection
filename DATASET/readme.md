**ALL ABOUT DATASET!**

**STEP1 -** 
A dataset with more than 1500 images of scanned documents containing various stamps and signatures was used for annotation purposes.

The src links for the dataset were:

1.   http://www.facweb.iitkgp.ernet.in/~jay/spods/
2.   http://madm.dfki.de/downloads-ds-staver


**STEP 2-**
These  ~1500 images are manually annotated using the labeling tool - OpenLabelling( src:https://github.com/Cartucho/OpenLabeling), by following below process:

o Creation of two classes: Signature and Stamp

o Rectangular bounding boxes were made around the signature and stamp locations of desired size(height & width)

o The annotated images are saved in the PASCAL_VOC and YOLO_darnet format.

**STEP 3-**

More images for creating the base training dataset (>5000 images) were created by various image augmentation techniques. Those includes:


1.     Converting to grayscale images ( to_gray.py ) (image(1089)-image(2176))

2.     Changing Brightness (to_change_bright.py) (image(2177)-image(3265))

3.     Changing contrast (to_contrast.py) (image(3266)-image(4353))

4.     Converting to HSL format (to_hls.py) (image(4354)-image(5440))


**STEP 4-**
The validation dataset created is around 900-1000 images, collected from the source:

1.     https://trai.gov.in/notifications/archive-tenders

2.     https://www.gsa.gov/real-estate/real-estate-services/leasing-policy-procedures/lease-documents/lease-documents-region-9-pacific-rim#California



The complete annotated dataset can be found by the links below!!

train dataset - https://drive.google.com/drive/folders/1r771FabcvkdrGgHrcv5tnrhOVKemks1L?usp=sharing

test dataset - https://drive.google.com/drive/folders/1rRjk7QL3jxtzCrTua3gQkEqE68lXmTwE?usp=sharing








