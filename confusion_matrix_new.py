import os
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from mlxtend.plotting import plot_confusion_matrix

CWD_PATH = os.getcwd()

import pandas
colnames = ['filename', 'stamp', 'signature']
data_pred = pandas.read_csv('object_counts.csv', names=colnames, header=0)

data_actual = pandas.read_csv('csv_counts_validationset.csv', names=colnames)


# data_actual = pandas.read_csv('csv_counts_validationset.csv', names=colnames)



filename_pred = data_pred.filename.tolist()
stamp_pred = data_pred.stamp.tolist()
signature_pred = data_pred.signature.tolist()
print("stamp_pred")
print(stamp_pred)


print("signature_pred")
print(signature_pred)

filename_act = data_actual.filename.tolist()
stamp_act = data_actual.stamp.tolist()
signature_act = data_actual.signature.tolist()

print("stamp_Act")
print(stamp_act)

print("signature_act")
print(signature_act)

import numpy as np
def conf_matrix(actual_list , pred_list):
    actual_list = np.asarray(actual_list)
    pred_list = np.asarray(pred_list)
    tp = len(np.where((((actual_list - pred_list) == 0 ) * (actual_list != 0)) == True)[0])
    tn = len(np.where((((actual_list - pred_list) == 0 )* (actual_list == 0)) == True)[0])
    fp = len(np.where((actual_list - pred_list) < 0 )[0])
    fn = len(np.where((actual_list - pred_list) > 0 )[0])

    output = np.full((2,2),np.nan)
    output[0,0] = tp 
    output[0,1] = fp
    output[1,0] = fn
    output[1,1] = tn
    
    accuracy_stamp = ((tp + tn)/(tp+tn+fn+fp)) * 100
    print( "accuarcy : ",accuracy_stamp)
    output = output.astype(np.int32)         
    return output


import matplotlib.pyplot as plt

print("stamp")
# print('True label')
# plt.xlabel('Predicted label')
# print('True label')

binary1 = conf_matrix(stamp_act,stamp_pred)

fig, ax = plot_confusion_matrix(conf_mat=binary1,
                                show_absolute=True,
                                show_normed=True,
                                colorbar=True)
plt.show()

print(conf_matrix(stamp_act,stamp_pred))

# classification report for precision, recall f1-score and accuracy
matrix_stamp = classification_report(stamp_act,stamp_pred)
print('Classification report : \n',matrix_stamp)


print("signature")
binary1 = conf_matrix(signature_act,signature_pred)

fig, ax = plot_confusion_matrix(conf_mat=binary1,
                                show_absolute=True,
                                show_normed=True,
                                colorbar=True)
plt.show()
print(conf_matrix(signature_act,signature_pred))

matrix_sign = classification_report(signature_act,signature_pred)
print('Classification report : \n',matrix_sign)
