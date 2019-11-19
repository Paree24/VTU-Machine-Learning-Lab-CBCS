from random import random,seed,randint
def initialize(n_inputs,n_hidden,n_output):
    network=[]
    hidden_layer=[{'w':[random() for i in range(n_inputs+1)]} for i in range(n_hidden)] #Initialize Weights and Biases for hidden layers
    network.append(hidden_layer)
    output_layer=[{'w':[random() for i in range(n_hidden+1)]} for i in range(n_output)] #Initialize Weights and Biases for output layer
    network.append(output_layer)
    return network
def activate(w,i):
    activation=w[-1] #Bias
    for x in range(len(w)-1):
        activation+=w[x]*i[x] #WX
        return activation #WX+B
from math import exp
def sigmoid(a):
    return 1/(1+exp(-a))
def forward_prop(network,row):
    inputs=row
    for layer in network:
        new_inputs=[]
        for neuron in layer:
            activation=activate(neuron['w'],inputs) #Compute Activations
            neuron['output']=sigmoid(activation) #Compute Sigmoid
            new_inputs.append(neuron['output']) 
        inputs=new_inputs
    return inputs
def sigmoid_derivative(output):
    return output * (1-output) #Derivative of 1/(1+e^-x)
def backprop(network,expected):
    for i in reversed(range(len(network))):
        layer=network[i]
        errors=[]
        if i!=len(network)-1: #Output Layer
            for j in range(len(layer)):
                error=0
                for neuron in network[i+1]:
                    error+=(neuron['w'][j]*neuron['delta'])
                errors.append(error)
        else:
                for j in range(len(layer)):
                    neuron=layer[j]
                    errors.append(expected[j]-neuron['output']) #Append Errors
        for j in range(len(layer)):
                neuron=layer[j]
                neuron['delta']=errors[j]*sigmoid_derivative(neuron['output']) #Compute Gradients
def update_weights(network,row,lrate): #Gradient Descent
    for i in range(len(network)):
        inputs=row[:-1]
        if i!=0:
            inputs=[neuron['output'] for neuron in network[i-1]]
            for neuron in network[i]:
                for j in range(len(inputs)):
                    neuron['w'][j]+=lrate*neuron['delta']*inputs[j] #Weights
                    neuron['w'][-1]+=lrate*neuron['delta'] #Bias
def train_network(network,train,lrate,epochs,n_output):
    for epoch in range(epochs):
        sum_err=0
        for row in train:
            outputs=forward_prop(network,row)
            expected=[0 for i in range(n_output)]
            expected[row[-1]]=1
            sum_err+=sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
            backprop(network,expected)
            update_weights(network,row,lrate)
        print('epoch=%d, lrate=%.3f,error=%.3f'%(epoch,lrate,sum_err))
seed(13)
data=[[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
n_inputs=len(data[0])-1
n_outputs=len(set(row[-1] for row in data))
network=initialize(n_inputs,2,n_outputs)
train_network(network,data,0.1,20,n_outputs)
for layer in network:
    print(layer)