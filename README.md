# stamp-signature-detection
Objective - To detect (localize &amp; classify) stamps and signatures in the scanned documents 

Process :
1. Dataset generation
2. models research and training
3. validation
4. output - bounding box generation



step1 - generate the csv files according to the test and train datasets - (xml_to_csv.py)
step2 - generate tfrecords for both - (generate_tfrecords.py)
step3 - config the model (training folder)
step4 - train the model - ( model_main.py)


