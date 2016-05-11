import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl
from sklearn import svm
from sklearn.metrics import accuracy_score

def svm_prediction_with_kernel(kernel_type):
	clf = svm.SVC(kernel=kernel_type)
	clf.fit(features_train, labels_train)

	predictions = clf.predict(features_test)
    	accuracy = accuracy_score(predictions, labels_test)
	print "[" + kernel_type + "] Accuracy: " + str(accuracy)

features_train, labels_train, features_test, labels_test = makeTerrainData()
svm_prediction_with_kernel('rbf')
svm_prediction_with_kernel('linear')
svm_prediction_with_kernel('poly')
svm_prediction_with_kernel('sigmoid')
	

#prettyPicture(clf, features_test, labels_test)
#plt.show()

