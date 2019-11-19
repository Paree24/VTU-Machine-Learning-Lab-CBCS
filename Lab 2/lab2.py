import csv
file=open('data.csv')
data=list(csv.reader(file))[1:]
concepts=[]
target=[]
for i in data:
    concepts.append(i[:-1])
    target.append(i[-1])
specific_h = concepts[0].copy()
general_h= [['?' for i in range(len(specific_h))] for i in range(len(specific_h))]
for i,h in enumerate(concepts):
    if target[i]=="yes":
        for x in range(len(specific_h)):
            if h[x]!=specific_h[x]:
                specific_h[x]='?'
                general_h[x][x] = '?'          
    if target[i]=="no":
        for x in range(len(specific_h)):
            if h[x]!= specific_h[x]:
                general_h[x][x]=specific_h[x]
            else:
                general_h[x][x]='?'   
indices=[i for i,val in enumerate(general_h) if val == ['?']*len(specific_h)]
for i in indices:
    general_h.remove(['?']*len(specific_h))
print("Final S:",specific_h,sep="\n")
print("Final G:",general_h,sep="\n")