import csv
file=open('data.csv')
data=list(csv.reader(file))
length=len(data[0])-1
h=['0']*length
print('Initial Hypothesis:',h,'\n')
print('Data:')
for i in data:
	print(i)
columns=data.pop(0)
for i in range(len(data)):
	if data[i][length]=='yes':
		for j in range(len(data[i])-1):
			if h[j]=='0':
				h[j]=data[i][j]
			if h[j]!=data[i][j]:
				h[j]='?'
print('\nFinal Hypothesis:',h)