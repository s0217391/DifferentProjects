#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = max( prey[0] , otherHunter[0] )
	temp2 = max( otherHunter[1] , temp0 )
	return [ otherHunter[1] , dist ]
