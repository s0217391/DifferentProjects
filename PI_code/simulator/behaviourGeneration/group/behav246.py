#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[1] )
	temp1 = -1 * dist
	if dist > otherHunter[0] :
		if dist != 0:
			temp2 = temp0 / dist
		else:
			temp2 = dist
	else:
		temp2 = otherHunter[1] - prey[0]
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	temp1 = min( otherHunter[1] , temp2 )
	return [ otherHunter[0] , prey[1] ]
