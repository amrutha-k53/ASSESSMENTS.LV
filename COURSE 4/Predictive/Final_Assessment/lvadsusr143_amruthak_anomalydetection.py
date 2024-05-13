# -*- coding: utf-8 -*-
"""LVADSUSR143_AMRUTHAK_AnomalyDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/116CkYpOQQZG6sswvEKvvTiRpldevuB6_
"""

import pandas as pd
df=pd.read_csv('/content/anomaly_train.csv')
df.head()

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()

from matplotlib import pyplot as plt
import seaborn as sns
figsize = (5, 0.2 * len(df['TransactionID'].unique()))
plt.figure(figsize=figsize)
plt.show()

sns.violinplot(df, x='Location', y='TransactionID', inner='stick', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

from sklearn.ensemble import IsolationForest
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
lbl_enc = LabelEncoder()
df['Type'] = lbl_enc.fit_transform(df['Type'])
df['Location'] = lbl_enc.fit_transform(df['Location'])

#ENCODING
encoded_df = pd.get_dummies(df[['Location','TransactionID']])

corr=df.corr()
sns.heatmap(corr,annot=True)

#Feature Scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
encoded_df = scaler.fit_transform(encoded_df)

#Fitting Isolation forest
clf=IsolationForest(n_estimators=100, max_samples='auto', \
                        max_features=1.0, bootstrap=False, n_jobs=-1, random_state=42, verbose=0)
clf.fit(encoded_df)

pred = clf.predict(encoded_df)
df['anomaly']=pred
outliers=df.loc[df['anomaly']==-1]
outlier_index=list(outliers.index)
#print(outlier_index)
#Find the number of anomalies and normal points here points classified -1 are anomalous
print(df['anomaly'].value_counts())

anomalies = df.loc[df["anomaly"] < 0]

# Create a scatter plot of suspicious activity vs social connections
plt.scatter(df["Amount"], anomalies['Amount'], label="Normal")
#plt.scatter(anomalies["Stress Level "], anomalies["anomaly"], color="r", label="Anomaly")
plt.xlabel("Location")
plt.ylabel("")
plt.legend()
plt.show()
