#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - otherHunter[1]
	if prey[1] != 0:
		temp1 = otherHunter[0] / prey[1]
	else:
		temp1 = prey[1]
	temp1 = prey[0] + otherHunter[1]
	temp2 = temp0 + dist
	temp1 = temp1 - otherHunter[1]
	temp0 = max( prey[0] , temp1 )
	temp2 = otherHunter[0] * temp1
	temp3 = temp1 + prey[1]
	if otherHunter[0] != 0:
		temp3 = otherHunter[1] % otherHunter[0]
	else:
		temp3 = otherHunter[0]
	if dist > otherHunter[1] :
		temp1 = min( prey[1] , prey[1] )
	else:
		if temp3 != 0:
			temp1 = prey[1] % temp3
		else:
			temp1 = temp3
	if temp2 != 0:
		temp1 = otherHunter[1] / temp2
	else:
		temp1 = temp2
	if temp1 != 0:
		temp4 = otherHunter[0] % temp1
	else:
		temp4 = temp1
	return [ temp3 , otherHunter[1] ]
