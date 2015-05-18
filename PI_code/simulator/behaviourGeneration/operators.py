#!/usr/bin/python
import random as r
import abc

def randomElementFromList(ellst):
	if(len(ellst) == 0):
		return 1
	ind = r.randint(0, len(ellst) - 1)
	return ellst[ind]


# get a random operand from a list of operands
def getOperand(ellst):
	if len(ellst) == 0:
		return r.randint(0, 100) * r.random()
	else:
		# right now set so it never uses a number
		if r.random() < -1.0:
			return r.randint(0, 100) * r.random()
		else:
			return randomElementFromList(ellst)

class op:
	'Abstract base class for operators'
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def printOperator(self, parlist, res):
		a = getOperand(parlist)
		return str(res) + " = " + str(a) + " "
		
class add(op):
	'plus operator'
	
	def printOperator(self, parlist, res):
		b = getOperand(parlist)
		result = super(add, self).printOperator(parlist, res)
		result = result + "+ " + str(b)
		return [(result, 0)]
		
		
class sub(op):
	'subtract operator'
	
	def printOperator(self, parlist, res):
		b = getOperand(parlist)
		result = super(sub, self).printOperator(parlist, res)
		result = result + "- " + str(b)
		return [(result, 0)]
		
class mul(op):
	'Mult operator'
	
	def printOperator(self, parlist, res):
		b = getOperand(parlist)
		result = super(mul, self).printOperator(parlist, res)
		result = result + "* " + str(b)
		return [(result, 0)]
				
class mini(op):
	'minimum operator'
	
	def printOperator(self, parlist, res):
		a = getOperand(parlist)
		b = getOperand(parlist)
		result =  str(res) + " = min(" + str(a) + ", " + str(b) + ")"
		return [(result, 0)]
				
class maxi(op):
	'maximum operator'
	
	def printOperator(self, parlist, res):
		a = getOperand(parlist)
		b = getOperand(parlist)
		result = str(res) + " = max(" + str(a) + ", " + str(b) + ")"
		return [(result, 0)]
	
				
class div(op):
	'divide operator'
	
	def printOperator(self, parlist, res):
		b = getOperand(parlist)
		result = super(div, self).printOperator(parlist, res)
		cond = "if " + str(b) + " != 0:"
		first = result + "/ " + str(b)
		els = "else:"
		second = str(res) + " = " + str(b)
		rslt = [(cond, 0), (first, 1), (els, 0), (second, 1)]
		return rslt
	
				
class mod(op):
	'modulus operator'
	
	def printOperator(self, parlist, res):
		b = getOperand(parlist)
		result = super(mod, self).printOperator(parlist, res)
		cond = "if " + str(b) + " != 0:"
		first = result + "% " + str(b)
		els = "else:"
		second = str(res) + " = " + str(b)
		rslt = [(cond, 0), (first, 1), (els, 0), (second, 1)]
		return rslt

class ifop(op):
	'if larger then operator'
	
	def printOperator(self, parlist, res):
		compareA = str(getOperand(parlist))
		compareB = str(getOperand(parlist))
		cond = "if " + compareA + " > " + compareB + ":"
		cond = [(cond, 0)]
		els = [("else:", 0)]
		expr1 = getRandOp().printOperator(parlist, str(res))
		expr1Added = []
		for x in expr1:
			(line, tabs) = x
			expr1Added.append((line, tabs+1))
		expr2 = getRandOp().printOperator(parlist, str(res))
		expr2Added = []
		for x in expr2:
			(line, tabs) = x
			expr2Added.append((line, tabs+1))
		result = cond + expr1Added + els  + expr2Added
		return result
		
class invertop(op):
	'invert a number'
	
	def printOperator(self, parlist, res):
		a = getOperand(parlist)
		result = str(res) + " = -1 * " + str(a)
		return [(result, 0)] 

def getRandOp():	
	ops = op.__subclasses__()
	ind = r.randint(0, len(ops) - 1)
	ope = ops[ind]()
	return ope
	
def getRandomOp(parlist, res):
	return getRandOp().printOperator(parlist, res)
	
def getReturnStatement(parlist):
	x = getOperand(parlist)
	y = getOperand(parlist)
	return [("return [" + x + ", " + y + "]", 0)]
	
