#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , otherHunter[1] )
	temp1 = prey[1] * prey[1]
	temp2 = temp0 + otherHunter[0]
	temp3 = max( temp0 , otherHunter[0] )
	temp1 = temp0 + prey[0]
	if temp2 != 0:
		temp3 = temp3 / temp2
	else:
		temp3 = temp2
	temp1 = min( otherHunter[1] , temp3 )
	return [ otherHunter[0] , temp1 ]
