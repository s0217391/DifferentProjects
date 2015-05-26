#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[1] :
		temp0 = otherHunter[1] + prey[0]
	else:
		if dist != 0:
			temp0 = prey[0] % dist
		else:
			temp0 = dist
	temp1 = max( dist , prey[1] )
	temp2 = otherHunter[0] + temp0
	temp1 = max( temp2 , otherHunter[0] )
	temp3 = temp1 + temp0
	if temp1 > prey[0] :
		temp4 = max( prey[1] , temp1 )
	else:
		temp4 = -1 * dist
	if otherHunter[0] != 0:
		temp5 = otherHunter[0] % otherHunter[0]
	else:
		temp5 = otherHunter[0]
	if temp3 != 0:
		temp4 = temp0 / temp3
	else:
		temp4 = temp3
	temp5 = temp4 * temp1
	temp1 = min( dist , dist )
	temp5 = temp0 + temp2
	temp4 = min( otherHunter[0] , otherHunter[1] )
	temp2 = -1 * temp2
	temp0 = temp1 * temp2
	temp6 = temp2 * temp3
	temp3 = temp5 + prey[0]
	temp4 = -1 * temp0
	temp1 = temp1 + prey[0]
	temp5 = otherHunter[0] + temp4
	return [ temp1 , temp4 ]
