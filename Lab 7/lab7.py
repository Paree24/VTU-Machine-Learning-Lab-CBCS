import pandas as pd,csv,numpy as np
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
attrs=list(csv.reader(open('data7_names.csv')))[0]
data=pd.read_csv('data7_heart.csv',names=attrs)
print("Head of Data:\n",data.head())
data=data.replace('?',np.nan)
model=BayesianModel([('age','trestbps'),('age','fbs'),('sex','trestbps'),
                     ('exang','trestbps'),('trestbps','heartdisease'),
                     ('fbs','heartdisease'),('heartdisease','restecg'),('heartdisease','thalach'),('heartdisease','chol')])
model.fit(data,estimator=MaximumLikelihoodEstimator)
data_infer=VariableElimination(model)
print('P(heartdisease|Age=20)')
q=data_infer.query(variables=['heartdisease'],evidence={'age':20})
print(q['heartdisease'])
print('P(heartdisease|cholestrol=100)')
q=data_infer.query(variables=['heartdisease'],evidence={'chol':100})
print(q['heartdisease'])
print('P(heartdisease|trestbps=12)')
q=data_infer.query(variables=['heartdisease'],evidence={'trestbps':12})
print(q['heartdisease'])