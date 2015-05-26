#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] > otherHunter[1] :
		temp0 = max( prey[0] , otherHunter[0] )
	else:
		if prey[0] > otherHunter[0] :
			if prey[1] > prey[1] :
				temp0 = otherHunter[0] - dist
			else:
				if otherHunter[1] != 0:
					temp0 = prey[0] / otherHunter[1]
				else:
					temp0 = otherHunter[1]
		else:
			temp0 = max( otherHunter[0] , otherHunter[1] )
	temp1 = prey[1] + otherHunter[1]
	temp2 = prey[1] * temp0
	temp0 = otherHunter[0] - temp2
	temp1 = max( temp1 , otherHunter[0] )
	temp1 = temp0 * dist
	if otherHunter[1] != 0:
		temp1 = otherHunter[1] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp0 = temp0 - temp0
	temp2 = prey[0] - temp0
	return [ otherHunter[1] , otherHunter[1] ]
