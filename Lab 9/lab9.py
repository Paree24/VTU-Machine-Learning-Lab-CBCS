from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
iris=datasets.load_iris()
xtrain,xtest,ytrain,ytest=train_test_split(iris.data,iris.target,test_size=0.3,random_state=0)
model=KNeighborsClassifier().fit(xtrain,ytrain)
pred=model.predict(xtest)
print("Accuracy: ",metrics.accuracy_score(ytest,pred))
plt.plot(xtest,ytest,'ro')
plt.plot(xtest,pred,'b+')