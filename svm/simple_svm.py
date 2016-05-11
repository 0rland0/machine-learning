import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl
from sklearn import svm
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()

clf = svm.SVC()
clf.fit(features_train, labels_train)

predictions = clf.predict(features_test)

# measure accuracy
accuracy = accuracy_score(predictions, labels_test)
print "Accuracy is: " + str(accuracy)

