The deployment script - inference_image1.py outputs :
1. json file (output cordinates foe each stamp/sig detection)
2. csv files containing - cordinates and no.of stamps and signatures



to run the script, use command :

!python inference_image1.py --input_folder=images/test               (or any other folder)


NOTE : The frozen_graph can be found in infernce_graph folder once the training and exporting generated inference graph is done.
Otherwise use this:

https://drive.google.com/drive/folders/1kT5X29DuihflcEqlaKAps66b90XaipvV?usp=sharing
