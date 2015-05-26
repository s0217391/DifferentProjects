#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , prey[1] )
	temp1 = temp0 * prey[1]
	temp0 = temp1 + otherHunter[0]
	temp2 = prey[0] * otherHunter[1]
	temp0 = temp2 + temp2
	if prey[1] != 0:
		temp1 = prey[1] / prey[1]
	else:
		temp1 = prey[1]
	temp1 = max( otherHunter[1] , otherHunter[0] )
	temp2 = -1 * prey[0]
	if temp2 > otherHunter[1] :
		temp3 = max( temp0 , dist )
	else:
		temp3 = max( dist , otherHunter[0] )
	temp1 = otherHunter[0] - temp1
	if prey[1] != 0:
		temp4 = prey[0] / prey[1]
	else:
		temp4 = prey[1]
	if temp1 > prey[0] :
		if temp2 != 0:
			temp5 = temp0 / temp2
		else:
			temp5 = temp2
	else:
		temp5 = max( temp2 , otherHunter[1] )
	if dist != 0:
		temp3 = otherHunter[0] % dist
	else:
		temp3 = dist
	temp2 = min( otherHunter[0] , prey[1] )
	if temp0 != 0:
		temp6 = dist / temp0
	else:
		temp6 = temp0
	return [ temp4 , temp2 ]
