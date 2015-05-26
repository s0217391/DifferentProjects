#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[0] :
		if otherHunter[1] > prey[1] :
			temp0 = dist + prey[0]
		else:
			temp0 = min( prey[1] , otherHunter[1] )
	else:
		temp0 = prey[0] * otherHunter[0]
	temp1 = otherHunter[0] + otherHunter[0]
	temp2 = otherHunter[1] + temp0
	temp1 = prey[0] * prey[1]
	temp3 = otherHunter[0] + prey[0]
	return [ temp1 , prey[0] ]
