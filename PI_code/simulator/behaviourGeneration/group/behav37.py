#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	if prey[0] > prey[1] :
		if otherHunter[1] != 0:
			temp1 = otherHunter[1] % otherHunter[1]
		else:
			temp1 = otherHunter[1]
	else:
		if otherHunter[0] > temp0 :
			temp1 = min( otherHunter[0] , otherHunter[1] )
		else:
			temp1 = prey[1] - prey[1]
	temp1 = min( prey[0] , otherHunter[0] )
	temp1 = temp1 - temp1
	temp1 = temp1 * dist
	temp0 = prey[1] * prey[1]
	temp1 = -1 * dist
	temp1 = dist - temp0
	if prey[1] != 0:
		temp0 = temp0 % prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[0] + prey[1]
	return [ otherHunter[1] , otherHunter[0] ]
