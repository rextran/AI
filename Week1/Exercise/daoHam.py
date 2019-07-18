def identity(): # f(x) = x
	return 1;
def logistic(x): #f(x)=1/(1+math.exp(-x))
	return math.exp(-x)/(1+math.exp(-x))**2
def tanh(x): #f(x)=tanh(x)=2/(1+math.exp(-2x)) - 1
	return 4*math.exp(-2*x)/(1+math.exp(-2*x))**2
def ReLU(x):
	# f(x)=0 if x<0, f(x)=x if x>=0
	if(x<0):
		return 0
	else:
		return 1
def PReLU(a,x):
	if(x<0):
		return a
	else:
		return 1
def ELU(a,x):
	if(x<0):
		return a*math.exp(x)
	else:
		return 1
def SoftPlus(x):
	return math.exp(x)/(1+math.exp(x))


