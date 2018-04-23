# Required Python Machine learning Packages
import pandas as pd
import numpy as np
# For preprocessing the data
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
# To split the dataset into train and test datasets
from sklearn.cross_validation import train_test_split
# To model the Gaussian Navie Bayes classifier
from sklearn.naive_bayes import GaussianNB
# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score



tennisData = pd.read_csv('Q2-tennis.csv',
                       header = None, delimiter=' *, *', engine='python')
t = tennisData

print(t)

t.columns = ['Outlook', 'Temp', 'Humidity', 'Windy', 'Play']

t = t.drop([0])

tennisdata = t

tennisdata_play = tennisdata.Play

OtherData = ['Outlook', 'Temp', 'Humidity', 'Windy']

DataForPrediction = tennisdata[OtherData]

t['Outlook1'] = [-1]*len(t.Outlook)
for s in range(0, len(t.Outlook)) :
  if t.Outlook[s+1]=="sunny":
      t.Outlook1[s+1]=0
  elif t.Outlook[s+1]=="overcast":
      t.Outlook1[s+1]=1
  elif t.Outlook[s+1]=="rainy":
      t.Outlook1[s+1]=2
  else:
      t.Outlook1[s+1]=3

t['Temp1'] = [-1]*len(t.Temp)
for s in range(0, len(t.Temp)) :
  if t.Temp[s+1]=="hot":
      t.Temp1[s+1]=0
  elif t.Temp[s+1]=="mild":
      t.Temp1[s+1]=1
  elif t.Temp[s+1]=="cool":
      t.Temp1[s+1]=2
  else:
      t.Temp1[s+1]=3

t['Humidity1'] = [-1]*len(t.Humidity)
for s in range(0, len(t.Humidity)) :
  if t.Humidity[s+1]=="high":
      t.Humidity1[s+1]=0
  elif t.Humidity[s+1]=="normal":
      t.Humidity1[s+1]=1
  else :
      t.Humidity1[s+1]=2

t['Windy1'] = [-1]*len(t.Windy)
for s in range(0, len(t.Windy)) :
  if t.Windy[s+1]=="true":
      t.Windy1[s+1]=1
  else :
      t.Windy1[s+1]=0

t['Play1'] = [-1]*len(t.Play)
for s in range(0, len(t.Play)) :
  if t.Play[s+1]=="yes":
      t.Play1[s+1]=1
  else :
      t.Play1[s+1]=0
 
print(t)
OtherData1 = ['Outlook1', 'Temp1', 'Humidity1', 'Windy1']
#for i in t:
  
tennisdata_play1 = tennisdata.Play1
#we get 15 sets to trained the model but we get the more accuracy from the below set
OtherData1 = [ 'Outlook1', 'Humidity1','Windy1' ]

DataForPrediction1 = tennisdata[OtherData1]

y = tennisdata_play1
X = DataForPrediction1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

gnb = GaussianNB()

y_pred_gnb = gnb.fit(X_train, y_train).predict(X_test)


print (y_pred_gnb)
print (X_train)
print (X_test)

print ("accuracy:",100*accuracy_score(y_test, y_pred_gnb))
