#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , otherHunter[1] )
	temp1 = prey[0] * prey[1]
	temp0 = -1 * otherHunter[0]
	temp0 = min( temp1 , otherHunter[0] )
	temp2 = max( prey[1] , otherHunter[0] )
	if dist > otherHunter[0] :
		if temp0 > prey[0] :
			temp3 = prey[1] * prey[0]
		else:
			if temp1 > prey[0] :
				temp3 = -1 * prey[1]
			else:
				temp3 = prey[0] + otherHunter[1]
	else:
		temp3 = max( prey[0] , dist )
	return [ temp3 , prey[0] ]
