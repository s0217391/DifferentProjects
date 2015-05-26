#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , prey[1] )
	temp1 = -1 * prey[0]
	if temp0 != 0:
		temp1 = prey[0] / temp0
	else:
		temp1 = temp0
	temp0 = otherHunter[1] - otherHunter[1]
	if temp1 > dist :
		if prey[0] > otherHunter[1] :
			if prey[1] != 0:
				temp0 = dist % prey[1]
			else:
				temp0 = prey[1]
		else:
			temp0 = max( otherHunter[0] , otherHunter[1] )
	else:
		temp0 = prey[1] * otherHunter[0]
	temp0 = temp0 + otherHunter[1]
	temp1 = -1 * temp1
	temp0 = min( otherHunter[1] , prey[0] )
	temp0 = max( otherHunter[1] , prey[1] )
	temp0 = temp0 + otherHunter[1]
	return [ temp0 , dist ]
