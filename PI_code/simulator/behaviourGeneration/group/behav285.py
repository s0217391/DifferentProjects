#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist * otherHunter[0]
	temp1 = max( prey[1] , prey[0] )
	temp1 = temp0 - otherHunter[1]
	return [ otherHunter[0] , dist ]
