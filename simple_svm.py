from sklearn import svm
# Features
X = [[0, 0], [1, 1]]

# Labels
y = [0, 1]

clf = svm.SVC()
clf.fit(X,y)

print clf.predict([[2., 2.]])
