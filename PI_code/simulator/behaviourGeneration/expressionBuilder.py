#!/usr/bin/python
import random as r
import operators as ops

var = ['prey[0]', 'prey[1]']
resultvar = []

def randomElementFromList(ellst):
	if(len(ellst) == 0):
		return 1
	ind = r.randint(0, len(ellst) - 1)
	return ellst[ind]

def getNewVar():
	tempNb = len(resultvar)
	newvar = 'temp' + str(tempNb)
	var.append(newvar)
	resultvar.append(newvar)
	return newvar

def selectResultVar():
	if len(resultvar) <= 1:
		return getNewVar()
	else:
		selector = r.randint(0, len(resultvar))
		if selector == len(resultvar):
			return getNewVar()
		else:
			return resultvar[selector]
			
def getOperand(ellst):
	if len(ellst) == 0:
		return r.randint(0, 100) * r.random()
	else:
		# right now set so it never uses a number
		if r.random() < -1.0:
			return r.randint(0, 100) * r.random()
		else:
			return randomElementFromList(var)

def buildSimpleExpression():
	a = getOperand(var)
	b = getOperand(var)
	resultVar = selectResultVar()
	return ops.getRandomOp(a, b, resultVar)

# generates a list of lines to be executed in order
def generateCodeBlock(maxlns = 10, seed = 0, minlns = 1):
	r.seed(seed)
	lines = r.randint(minlns, maxlns)
	result = []
	for i in range(lines):
		result = result + buildSimpleExpression()
	x = getOperand(var)
	y = getOperand(var)
	result.append("return np.array([" + x + ", " + y + "])")
	return result
