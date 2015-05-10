#!/usr/bin/python
import random as r
import operators as ops

var = []

def randomElementFromList(ellst):
	if(len(ellst) == 0):
		return 1
	ind = r.randint(0, len(ellst) - 1)
	return ellst[ind]

def getNewVar():
	tempNb = len(var)
	newvar = 'temp' + str(tempNb)
	var.append(newvar)
	return newvar

def selectResultVar():
	if len(var) <= 1:
		return getNewVar()
	else:
		selector = r.randint(0, len(var))
		if selector == len(var):
			return getNewVar()
		else:
			return var[selector]
			
def getOperand(ellst):
	if len(ellst) == 0:
		return r.randint(0, 100) * r.random()
	else:
		if r.random() < 0.2:
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
	result.append("print " + var[len(var) - 1])
	return result
