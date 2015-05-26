#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + otherHunter[1]
	if dist > prey[1] :
		temp1 = min( temp0 , temp0 )
	else:
		if otherHunter[0] != 0:
			temp1 = otherHunter[0] % otherHunter[0]
		else:
			temp1 = otherHunter[0]
	temp0 = max( prey[0] , otherHunter[1] )
	temp0 = temp0 - temp0
	if otherHunter[0] != 0:
		temp2 = prey[0] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp0 = prey[0] - prey[0]
	temp1 = min( temp0 , otherHunter[1] )
	temp0 = min( otherHunter[0] , prey[0] )
	temp3 = min( prey[1] , dist )
	temp0 = min( prey[0] , temp1 )
	temp0 = otherHunter[0] + dist
	if prey[1] > temp0 :
		temp2 = prey[0] + otherHunter[1]
	else:
		temp2 = -1 * otherHunter[0]
	if temp2 != 0:
		temp2 = prey[1] / temp2
	else:
		temp2 = temp2
	return [ temp0 , temp0 ]
