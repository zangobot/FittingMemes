import os, sys
import numpy as np
import pickle
from skimage.io import imread
from skimage.transform import resize
from scipy import signal
from sklearn.model_selection import StratifiedShuffleSplit

# file * --mime-type | grep html | awk '{print $1}' | tr -d ":" | xargs rm
# Use this command to remove images which are downloaded as html

def generate_mapping():
    classes = {}
    data = []
    for file in os.listdir("data"):
        name = file.split('.')[0]
        if name not in classes:
            classes[name] = len(classes)
        assigned_class = classes[name]
        data.append([file, assigned_class])
    return data, classes

def create_dataset(data, n_classes, persistance = True):
    X, Y = [], []
    if os.path.isfile('train_data') and os.path.isfile('train_labels'):
        with open('train_data','rb') as tr_data:
            X = pickle.load(tr_data)
        with open('train_labels','rb') as tr_data:
            Y = pickle.load(tr_data)
    else:
        for d in data:
            path = os.path.join('data',d[0])
            try:
                im = imread(path, as_grey=True)
                im = resize(im, (200,200)).ravel()
                X.append( im )
                # Y.append( signal.unit_impulse(n_classes, d[1]) )
                Y.append( d[1] )
            except:
                print(sys.exc_info())
        X, Y = np.array(X), np.array(Y)
        if persistance:
            with open('train_data','wb') as tr_data:
                pickle.dump(X, tr_data)
            with open('train_labels','wb') as tr_label:
                pickle.dump(Y, tr_label)

    
    return X, Y


def train_test_split(test_size = 0.25, subsample=1, persistance= True, X=None, Y = None):
    if X is None or Y is None:
        data, classes = generate_mapping()
        X, Y = create_dataset(data, len(classes), persistance=persistance)
    subsize = int(subsample * len(Y))
    choice = np.random.choice( range(len(Y)),subsize)
    X, Y = X[choice], Y[choice]
    stratsplit =  StratifiedShuffleSplit(10, test_size=test_size)
    for tr_index, ts_index in stratsplit.split(X,Y):
        X_train, Y_train = X[tr_index], Y[tr_index]
        X_tst, Y_tst = X[ts_index], Y[ts_index]
        break
    return X_train, Y_train, X_tst, Y_tst


