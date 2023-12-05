import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data=pd.read_csv('/content/marine debris remote sensing with year.csv')
data.columns
data[data.isnull().any(axis=1)].head()
data=data.dropna()
data.shape
clean_data=data.copy()
clean_data['ItemName']=(clean_data['Quantity'])*1
clean_data['ItemName'].head()
y=clean_data[['ItemName']].copy()
y.head()
train_features = ['Quantity']
x=clean_data[train_features].copy()
x.columns
from sklearn.preprocessing import LabelEncoder
LabelEncoder_x = LabelEncoder()
x = x.apply(LabelEncoder().fit_transform)
x
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=324)
Action_classifier=DecisionTreeClassifier(max_leaf_nodes=10,random_state=0)
Action_classifier.fit(X_train,y_train)
y_predicted=Action_classifier.predict(X_test)
accuracy_score(y_test,y_predicted)*100
confusion_matrix(y_test,y_predicted)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
plot_tree(Action_classifier, filled=True, feature_names=x.columns, class_names=label_encoder.classes_)
plt.show()
