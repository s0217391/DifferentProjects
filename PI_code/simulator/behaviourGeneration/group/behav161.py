#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , otherHunter[0] )
	temp1 = max( dist , prey[1] )
	temp0 = otherHunter[1] + otherHunter[0]
	if temp1 > prey[0] :
		if prey[1] != 0:
			temp2 = dist / prey[1]
		else:
			temp2 = prey[1]
	else:
		temp2 = dist + otherHunter[0]
	if temp2 != 0:
		temp0 = temp1 / temp2
	else:
		temp0 = temp2
	return [ dist , prey[0] ]
