#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + prey[0]
	temp1 = min( prey[0] , prey[0] )
	if otherHunter[0] > otherHunter[0] :
		if temp0 != 0:
			temp1 = otherHunter[0] % temp0
		else:
			temp1 = temp0
	else:
		temp1 = max( temp1 , prey[0] )
	temp0 = prey[1] - temp0
	return [ otherHunter[1] , otherHunter[1] ]
