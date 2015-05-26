#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * otherHunter[0]
	if prey[1] != 0:
		temp1 = otherHunter[0] / prey[1]
	else:
		temp1 = prey[1]
	if temp0 > prey[0] :
		temp2 = -1 * dist
	else:
		if otherHunter[0] > prey[0] :
			temp2 = temp1 * prey[0]
		else:
			temp2 = min( prey[1] , prey[1] )
	temp2 = dist + prey[0]
	if dist != 0:
		temp3 = prey[1] / dist
	else:
		temp3 = dist
	temp1 = min( otherHunter[1] , otherHunter[0] )
	temp2 = -1 * temp2
	temp2 = temp1 - temp1
	temp4 = prey[0] - temp0
	temp4 = max( prey[0] , temp2 )
	temp4 = max( otherHunter[0] , temp0 )
	temp5 = max( otherHunter[0] , dist )
	temp3 = temp5 - temp3
	temp1 = max( prey[0] , temp0 )
	if temp0 != 0:
		temp1 = temp3 / temp0
	else:
		temp1 = temp0
	if temp3 != 0:
		temp4 = prey[1] % temp3
	else:
		temp4 = temp3
	temp0 = min( temp5 , temp5 )
	temp3 = temp3 * otherHunter[1]
	temp1 = max( dist , temp5 )
	temp4 = min( temp1 , otherHunter[0] )
	temp5 = min( temp0 , temp1 )
	temp5 = temp5 - dist
	temp2 = prey[1] + prey[0]
	temp5 = prey[1] - otherHunter[1]
	temp2 = -1 * temp3
	return [ otherHunter[1] , temp2 ]
