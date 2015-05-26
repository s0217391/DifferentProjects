#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , otherHunter[0] )
	temp1 = prey[1] - prey[1]
	temp2 = prey[0] + otherHunter[0]
	if dist > prey[0] :
		temp0 = temp2 * temp2
	else:
		if temp0 != 0:
			temp0 = prey[1] % temp0
		else:
			temp0 = temp0
	temp2 = -1 * otherHunter[0]
	temp3 = -1 * temp1
	temp4 = -1 * temp1
	temp4 = temp4 + dist
	temp5 = prey[1] * temp3
	temp5 = max( temp0 , otherHunter[1] )
	temp2 = otherHunter[1] * temp4
	if temp3 > prey[0] :
		temp6 = min( otherHunter[0] , temp2 )
	else:
		temp6 = max( temp4 , temp5 )
	temp4 = min( dist , temp4 )
	temp0 = min( temp2 , dist )
	return [ prey[0] , dist ]
