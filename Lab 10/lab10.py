import numpy as np
import matplotlib.pyplot as plt
xtrain=np.array(list(range(3,35))).reshape(32,1)
ytrain=np.sin(xtrain)+xtrain**0.75
xtest=np.array([i/10 for i in range(400)]).reshape(400,1)
ytest=[]
for r in range(len(xtest)):
    w=np.diag(np.exp(-np.sum((xtrain-xtest[r])**2,axis=1)/(2*0.5**2)))
    f1=np.linalg.inv(xtrain.T.dot(w).dot(xtrain))
    params=f1.dot(xtrain.T).dot(w).dot(ytrain)
    pred=xtest[r].dot(params)
    ytest.append(pred)
plt.plot(xtrain,ytrain,'o')
plt.plot(xtest,ytest,'-')  