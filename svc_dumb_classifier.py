from data_generator import  train_test_split, generate_mapping, create_dataset
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedShuffleSplit
import numpy as np
import matplotlib.pyplot as plt

X_train, y_train, X_tst, y_tst = train_test_split(test_size=0.7, subsample=1, persistance=False)
print("The shape of the problem is {}".format(X_train.shape))

grid = {
    'gamma' : np.logspace(-1,1,10),
    'C' : np.logspace(-1,1,10)
}

gscv = GridSearchCV( SVC(kernel='rbf') , param_grid=grid, cv=StratifiedShuffleSplit(n_splits=10,test_size=0.25))
gscv.fit(X_train, y_train)

clf = gscv.best_estimator_

y_pred = clf.predict(X_tst)

error =  100*np.sum( y_pred != y_tst ) / len(y_tst)
print('This time the error is {0:.2f}'.format(error))

result = np.sort(clf.coef_)
result = result[::-1]
plt.semilogy(result[:300])
plt.title('Importance of features')
plt.xlabel('Ordered features')
plt.ylabel('Importance')
plt.show()