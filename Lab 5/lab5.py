import csv,math,random,statistics
random.seed(10)
def prob(x,mean,stdev):
    e=math.exp(-(math.pow(x-mean,2))/(2*math.pow(stdev,2)))
    return (1/(math.sqrt(2*math.pi)*stdev))*e
file=open('data.csv')
data=[[float(a) for a in row] for row in csv.reader(file)]
print('Size of dataset is: ',len(data))
train_indices=random.sample(range(len(data)),int(0.7*len(data)))
xtrain=[data[i] for i in train_indices]
xtest=[data[i] for i in range(len(data)) if i not in train_indices]
classes={}
for samples in xtrain:
    last=int(samples[-1])
    if last not in classes:
        classes[last]=[]
    classes[last].append(samples)
summaries={}
for classVal,traindata in classes.items():
    summary=[(statistics.mean(attr),statistics.stdev(attr)) for attr in zip(*traindata)]
    del summary[-1]
    summaries[classVal]=summary
prediction=[]
for test in xtest:
    probs={}
    for classVal,summary in summaries.items():
        probs[classVal]=1
        for i,attr in enumerate(summary):
            probs[classVal]*=prob(test[i],attr[0],attr[1])
        bestlabel,bestprob=None,0
    for classVal,p in probs.items():
        if bestlabel is None or p>bestprob:
            bestprob=p
            bestlabel=classVal
    prediction.append(bestlabel)
correct=0
for i,key in enumerate(xtest):
    if xtest[i][-1]==prediction[i]:
        correct+=1
print("Accuracy: ",correct*100/len(xtest))