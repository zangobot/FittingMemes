from data_generator import  train_test_split
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X_train, y_train, X_tst, y_tst = train_test_split(test_size=0.8, subsample=1, persistance=False)

print("LET'S LEARN THIS DUMB CLASSIFIER")
print("The shape of the problem is {}".format(X_train.shape))

forest = RandomForestClassifier(n_estimators=15)
forest.fit(X_train, y_train)

y_pred = forest.predict(X_tst)

error =  100*np.sum( y_pred != y_tst ) / len(y_tst)

print('And the error is ONLY {0:.2f} %!'.format(error))