pendigits
=========

A mirror of the pendigits datasets from http://mkl.ucsd.edu/dataset/pendigits

Representation information
--------------------------
The pendigits data set is on pen-based digit recognition (multiclass classification with 10 classes) and contains four different feature representations. The feature representations (D is the number of features) are: 

* dyn (D = 16): eight successive pen points on two-dimensional coordinate system.
* sta16 (D = 256): 16 x 16 image bitmap representation formed by connecting the points * in dyn representation with line segments.
* sta8 (D = 64): 8 x 8 subsampled bitmap representation.
* sta4 (D = 16): 4 x 4 subsampled bitmap representation.

Files
-----
* pendigits_dyn_train.csv: training instances in dyn representation.
* pendigits_dyn_test.csv: test instances in dyn representation.
* pendigits_sta16_train.csv: training instances in sta16 representation.
* pendigits_sta16_test.csv: test instances in sta16 representation.
* pendigits_sta8_train.csv: training instances in sta8 representation.
* pendigits_sta8_test.csv: test instances in sta8 representation.
* pendigits_sta4_train.csv: training instances in sta4 representation.
* pendigits_sta4_test.csv: test instances in sta4 representation.
* pendigits_label_train.csv: class labels of training instances.
* pendigits_label_test.csv: class labels of test instances.

Manipulation
------------

There's a python script in there to combine the inputs and targets into a json file.

Example Usage:
* To get sta16 representation of training data into a file named data.json
```
python combine.py --representation sta16 --type train > data.json
```
* To get sta4 representation of test data into a file named data.json
```
python combine.py --representation sta4 --type test > data.json
```

Alternative sources
-------------------
The dyn representation can also be downloaded from the UCI Machine Learning Repository (http://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits). [alimoglu97icdar] Alimoglu, F., & Alpaydin E. (1997).  Combining Multiple Representations and Classifiers for Pen-based Handwritten Digit Recognition. Fourth International Conference on Document Analysis and Recognition (ICDAR 97). [demir05prl] Demir, C., & Alpaydin E. (2005).  Cost-Conscious Classifier Ensembles. Pattern Recognition Letters. 26(14), 2206-2214.  [gonen10prl] Gonen, M., & Alpaydin E. (2010).  Cost-Conscious Multiple Kernel Learning. Pattern Recognition Letters. 31(9), 959-965.


