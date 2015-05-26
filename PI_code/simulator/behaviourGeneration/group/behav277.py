#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - dist
	if otherHunter[0] != 0:
		temp1 = otherHunter[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if otherHunter[1] != 0:
		temp0 = prey[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = min( prey[1] , temp0 )
	temp2 = min( otherHunter[1] , dist )
	temp0 = temp2 * temp0
	temp2 = -1 * prey[1]
	temp1 = max( temp2 , prey[0] )
	temp1 = max( dist , otherHunter[1] )
	if prey[1] > otherHunter[1] :
		if otherHunter[1] != 0:
			temp3 = otherHunter[1] % otherHunter[1]
		else:
			temp3 = otherHunter[1]
	else:
		temp3 = max( otherHunter[0] , prey[1] )
	temp4 = prey[1] - dist
	return [ dist , temp4 ]
