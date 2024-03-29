# -*- coding: utf-8 -*-
"""breast_cancer_detection.ipnyb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JkeGERcHYXHl18ofQoEHdSDYeFA2EavL
"""

import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data = pd.read_csv("data.csv")
data = data.drop(['id'], axis=1)

plt.hist(data["radius_mean"])
plt.show()

plt.hist(data["diagnosis"])
plt.show()

plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(data.corr(), vmax=1, vmin=-1, annot=True)
heatmap.set_title("Correlation in Breast Cancer Dataset")
plt.show()

#
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
label_encoder = LabelEncoder()
min_max_scaler = MinMaxScaler()
data["diagnosis"] = label_encoder.fit_transform(data["diagnosis"])
X = data[["radius_mean", "perimeter_mean", "area_mean", "concavity_mean", "concave_points_mean",
          "radius_worst", "perimeter_worst", "area_worst", "concave_points_worst"]].values
X = min_max_scaler.fit_transform(X)
y = data["diagnosis"].values


#0 is Benign, 1 is Malignant

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
y_test.shape

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(9,)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='Adam', loss='BinaryCrossentropy', metrics=['accuracy'])

epochs_hist = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100)

epochs_hist.history.keys()

plt.plot(epochs_hist.history["accuracy"], 'blue', label="Training Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Epochs v Accuracy")
plt.plot(epochs_hist.history["val_accuracy"], 'red', label="Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Val Accuracy")
plt.title("Epochs v Val Accuracy")
plt.legend()
plt.show()

plt.plot(epochs_hist.history["loss"], 'blue', label="Training Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Epochs v Loss")
plt.plot(epochs_hist.history["val_loss"], 'red', label="Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Val Loss")
plt.title("Epochs v Val Loss")
plt.legend()
plt.show()

