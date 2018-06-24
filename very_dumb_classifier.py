from data_generator import  train_test_split, generate_mapping, create_dataset
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt

X_train, y_train, X_tst, y_tst = train_test_split(test_size=0.7, subsample=1, persistance=False)
print("The shape of the problem is {}".format(X_train.shape))

forest = RandomForestClassifier(n_estimators=15)
forest.fit(X_train, y_train)

y_pred = forest.predict(X_tst)

error =  100*np.sum( y_pred != y_tst ) / len(y_tst)

print('And the error is ONLY {0:.2f} %!'.format(error))
result = np.sort(forest.feature_importances_)
result = result[::-1]
plt.semilogy(result[:300])
plt.title('Importance of features')
plt.xlabel('Ordered features')
plt.ylabel('Importance')
