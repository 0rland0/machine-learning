from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from prep_terrain_data import makeTerrainData


features_train, labels_train, features_test, labels_test = makeTerrainData()
clf = GaussianNB()
clf = clf.fit(features_train, labels_train)
predictions = clf.predict(features_test)
acc = accuracy_score(labels_test, predictions)
print acc



