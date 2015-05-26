#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , prey[0] )
	if prey[0] != 0:
		temp1 = otherHunter[1] / prey[0]
	else:
		temp1 = prey[0]
	if prey[0] > prey[0] :
		temp2 = max( temp1 , otherHunter[1] )
	else:
		temp2 = -1 * temp1
	temp2 = max( prey[0] , prey[1] )
	temp2 = temp1 * dist
	temp2 = otherHunter[0] - temp2
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	return [ prey[1] , temp1 ]