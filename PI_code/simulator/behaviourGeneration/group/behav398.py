#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , dist )
	temp1 = otherHunter[1] * prey[0]
	if dist > otherHunter[1] :
		if temp0 != 0:
			temp2 = otherHunter[1] / temp0
		else:
			temp2 = temp0
	else:
		temp2 = max( dist , otherHunter[1] )
	temp0 = max( temp0 , dist )
	temp3 = min( prey[1] , temp0 )
	return [ temp1 , otherHunter[0] ]
