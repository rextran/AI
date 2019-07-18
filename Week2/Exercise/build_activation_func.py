import math
import numpy
import random
from matplotlib import pyplot as plt
def sigmoid(x):
	return 1/(1 + math.exp(-x))


def tanh(x):
	return 2/(1 + math.exp(-2*x)) - 1

def ReLU(x):
	if(x < 0):
		return 0
	else:
		return x
def PReLU(a, x):
	if(x < 0):
		return a*x
	else:
		return x
def ELU(a,x):
	if(x < 0):
		return a*(math.exp(x) - 1)
	else:
		return x
def softPlus(x):
	return math.log(1 + math.exp(x))
N = 100
sig = []
tan = []
relu = []
prelu = []
elu = []
softplus = []
for j in range(-N, N):
	a = 0.1
	i = j/10.0
	sig.append(sigmoid(i))
	tan.append(tanh(i))
	relu.append(ReLU(i))
	prelu.append(PReLU(a,i))
	elu.append(ELU(a,i))
	softplus.append(softPlus(i))
plt.subplot(321)
plt.plot(sig)
plt.ylabel("sigmoid")
plt.subplot(322)
plt.plot(tan)
plt.ylabel("tan")
plt.subplot(323)
plt.plot(relu)
plt.ylabel("ReLU")
plt.subplot(324)
plt.plot(prelu)
plt.ylabel("PReLU")
plt.subplot(325)
plt.plot(elu)
plt.ylabel("ELU")
plt.subplot(326)
plt.plot(softplus)
plt.ylabel("softPlus")

plt.show()