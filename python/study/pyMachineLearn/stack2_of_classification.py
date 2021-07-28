#! WARNING: this py file is not intended for running!
import numpy as np
import pandas as pd
import matplotlib as mpl                  
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

#feching-data:
def sort_by_target(mnist):
    reorder_train = np.array(sorted([(target, i) for i, target in enumerate(mnist.target[:60000])]))[:, 1]
    reorder_test = np.array(sorted([(target, i) for i, target in enumerate(mnist.target[60000:])]))[:, 1]
    mnist.data[:60000] = mnist.data[reorder_train]
    mnist.target[:60000] = mnist.target[reorder_train]
    mnist.data[60000:] = mnist.data[reorder_test + 60000]
    mnist.target[60000:] = mnist.target[reorder_test + 60000]
try:
    from sklearn.datasets import fetch_openml
    mnist = fetch_openml('mnist_784', version=1, cache=True, as_frame=False)
    mnist.target = mnist.target.astype(np.int8) # fetch_openml() returns targets as strings
    sort_by_target(mnist) # fetch_openml() returns an unsorted dataset
except ImportError:
    from sklearn.datasets import fetch_mldata
    mnist = fetch_mldata('MNIST original')

def plot_digit(data):
    image = data.reshape(28, 28)
    plt.imshow(image, cmap = mpl.cm.binary,
               interpolation="nearest")
    plt.axis("off")


X ,y = mnist["data"], mnist["target"]
X_train , X_test , y_train , y_test = X[:60000],X[60000:],y[:60000],y[60000:]

shuffled_index = np.random.permutation(60000)
X_train , y_train = X_train[shuffled_index] , y_train[shuffled_index]

#   binary classifier: is 5 ?
y_train_is5 = (y_train == 5)
y_train_not5 = (y_train != 5) #! cannot be y_train_is5 = y_train[y_train == 5]

from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier()
sgd_clf.fit( X_train , y_train_is5 )

sgd_clf.predict([X[1000]])

#   Assessments
#--- Using cross-val again:
    #default:
from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf , X_train , y_train ,cv =3 ,scoring = 'accuracy')

    # more free:
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone

skfolds = StratifiedKFold(n_splits=3, random_state=42, shuffle=True)

for train_index, test_index in skfolds.split(X_train, y_train_is5):
    clone_clf = clone(sgd_clf)

    X_train_folds = X_train[train_index]
    y_train_folds = (y_train_is5[train_index])
    X_test_fold = X_train[test_index]
    y_test_fold = (y_train_is5[test_index])  #split-reindex

    clone_clf.fit(X_train_folds, y_train_folds) #train

    y_pred = clone_clf.predict(X_test_fold)   #calc points
    n_correct = sum(y_pred == y_test_fold)
    print(n_correct / len(y_pred))

#write a classifier:?
from sklearn.base import BaseEstimator
class Never5Classifier(BaseEstimator):
    def fit(self, X, y=None):
        pass
    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)


#Confusion matrix:  classification assessment
# predict points -> matrix
from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sgd_clf,X_train,y_train_is5,cv=3)
    #every predict is 'clean' because the sample is never seen
# build matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_train_is5 ,y_train_pred)
#    row: ture classifications , lines: pred classification


#3 new scores:
#recall : true positive / true positive + false negative "don't let false pass"
#sencitivity : true positive / true positive + false positive  "don't let true go away"
#f1 : tiao he ping jun zhi of recall&sensitivity


#setting up its thresthold: indirect ---- decision_function:
scores = sgd_clf.decision_function()
    # default threshhold is 0
    #use other threshold:
pred = (scores > 10000 )#threshold num

    # to sure this threshold
#1 get all scores:
y_scores = cross_val_predict(sgd_clf,X_train,y_train_is5,cv = 3 , method="decision_function") 
#2 plot curve:
from sklearn.metrics import precision_recall_curve    #just calulation
pre , rec , thresh = precision_recall_curve(y_train_is5,y_scores)

def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision", linewidth=2)
    plt.plot(thresholds, recalls[:-1], "g-", label="Recall", linewidth=2)
    plt.xlabel("Threshold", fontsize=16)
    plt.legend(loc="upper left", fontsize=16)
    plt.ylim([0, 1])


#Meanwhile, ROC curve: almost the same:
from sklearn.metrics import roc_curve
fpr , tpr , thresh = roc_curve(y_train_is5, y_scores)
    #calulate its Area by:
from sklearn.metrics import roc_auc_score
roc_auc_score(y_train_is5, y_scores)

    #for RandomFroestclassifiers:, use dict_proba instead of desicition_function:
from sklearn.ensemble import RandomForestClassifier
forest_clf = RandomForestClassifier()
y_pro = cross_val_predict(forest_clf , X_train , y_train_is5 , cv= 3 , method= 'predict_proba')
    #pick positive probability:
y_scores = y_pro[:,:1]




#Multiclass classification:
#Randomforest & baes --auto multiclass , for bin-only classifiers:
#One vs All: build classifier for each:(prefered in sklearn)
#One vs one: build classifier for each 2 classes

#forcing ovo or ova:
from sklearn.multiclass import OneVsOneClassifier , OneVsRestClassifier
    # and put themoutside the classifier


#Analyzing the errors:
#1 confusion matrix:
con_m = confusion_matrix(y_train,y_pred)
plt.matshow(con_m , cmap = plt.cm.gray)#use plt.cm.grey, show general
row_sums = con_m.sum(axis = 1, keep_dims = True)#focus on errors:
norm_con_m = con_m / row_sums


#Multilabels classification / MultiOutput Classification









