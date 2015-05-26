#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , otherHunter[0] )
	temp1 = otherHunter[1] - dist
	temp1 = max( prey[0] , otherHunter[0] )
	if temp1 != 0:
		temp2 = prey[1] / temp1
	else:
		temp2 = temp1
	temp1 = -1 * dist
	temp3 = otherHunter[0] - otherHunter[1]
	temp0 = temp1 - prey[0]
	if prey[0] != 0:
		temp3 = temp2 / prey[0]
	else:
		temp3 = prey[0]
	temp1 = prey[0] + temp1
	temp3 = otherHunter[0] + temp1
	if prey[1] != 0:
		temp2 = temp3 % prey[1]
	else:
		temp2 = prey[1]
	temp0 = prey[0] - temp1
	temp4 = max( temp3 , otherHunter[1] )
	temp4 = -1 * dist
	if temp3 > prey[1] :
		temp4 = otherHunter[0] - temp0
	else:
		temp4 = dist * dist
	return [ temp0 , prey[0] ]
