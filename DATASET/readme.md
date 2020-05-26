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


1.     Converting to grayscale images ( to_gray.py )

2.     Changing Brightness (to_change_bright.py)

3.     Changing contrast (to_contrast.py)

4.     Resizing the images(~(320 * 570))


**STEP 4-**
The validation dataset created is around 900-1000 images, collected from the source:

1.     https://trai.gov.in/notifications/archive-tenders

2.     https://www.gsa.gov/real-estate/real-estate-services/leasing-policy-procedures/lease-documents/lease-documents-region-9-pacific-rim#California



The complete annotated and augmented training dataset can be found by the links below!!

train dataset - https://drive.google.com/open?id=1gWNaAab_oz9ooikHr2ABD5rQVwTgQgxB

test dataset - https://drive.google.com/open?id=1gx7ge-xINPGMFexqmztisj4DAR3-rnQ2



# SUGGESTION: Make a folder named images(in object_detection folder) that contains 2 folders train and test , both containing the respective image datasets aalong with their respective XML and if needed YOLO(.txt) annotated files.







