#!/usr/bin/python
import random as r
import abc

class op:
	'Abstract base class for operators'
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def printOperator(self, a, b, res):
		return str(res) + " = " + str(a) + " "
		
class add(op):
	'plus operator'
	
	def printOperator(self, a, b, res):
		result = super(add, self).printOperator(a, b, res)
		result = result + "+ " + str(b)
		return [result]
		
		
class sub(op):
	'subtract operator'
	
	def printOperator(self, a, b, res):
		result = super(sub, self).printOperator(a, b, res)
		result = result + "- " + str(b)
		return [result]
		
class mul(op):
	'Mult operator'
	
	def printOperator(self, a, b, res):
		result = super(mul, self).printOperator(a, b, res)
		result = result + "* " + str(b)
		return [result]
				
class mini(op):
	'minimum operator'
	
	def printOperator(self, a, b, res):
		result =  str(res) + " = min(" + str(a) + ", " + str(b) + ")"
		return [result]
				
class maxi(op):
	'maximum operator'
	
	def printOperator(self, a, b, res):
		result = str(res) + " = max(" + str(a) + ", " + str(b) + ")"
		return [result]
	
				
class div(op):
	'divide operator'
	
	def printOperator(self, a, b, res):
		result = super(div, self).printOperator(a, b, res)
		cond = "if " + str(b) + " != 0: "
		first = cond + result + "/ " + str(b)
		second = "else: " + str(res) + " = " + str(a)
		rslt = [first, second]
		return rslt
	
				
class mod(op):
	'modulus operator'
	
	def printOperator(self, a, b, res):
		result = super(mod, self).printOperator(a, b, res)
		cond = "if " + str(b) + " != 0: "
		first = cond + result + "% " + str(b)
		second = "else: " + str(res) + " = " + str(a)
		rslt = [first, second]
		return rslt


def getRandomOp(a, b, res):
	ops = op.__subclasses__()
	ind = r.randint(0, len(ops) - 1)
	ope = ops[ind]()
	return ope.printOperator(a, b, res)
