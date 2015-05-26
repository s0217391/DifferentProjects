#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > prey[1] :
		if dist > otherHunter[0] :
			temp0 = max( dist , prey[1] )
		else:
			temp0 = min( prey[1] , prey[0] )
	else:
		temp0 = dist * prey[0]
	temp1 = -1 * prey[1]
	if otherHunter[1] != 0:
		temp1 = temp0 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[0] != 0:
		temp1 = prey[1] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if otherHunter[1] > otherHunter[0] :
		temp1 = dist * temp1
	else:
		temp1 = min( dist , temp0 )
	temp2 = -1 * dist
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	temp3 = -1 * temp2
	temp0 = temp3 * temp0
	if temp3 > otherHunter[1] :
		temp3 = min( temp1 , temp2 )
	else:
		temp3 = max( temp2 , temp3 )
	temp2 = max( prey[0] , temp0 )
	if temp0 != 0:
		temp1 = otherHunter[1] % temp0
	else:
		temp1 = temp0
	temp1 = temp3 + temp0
	temp1 = min( prey[1] , prey[1] )
	temp3 = max( otherHunter[0] , dist )
	temp0 = temp1 + temp0
	temp3 = otherHunter[0] * prey[0]
	if otherHunter[1] != 0:
		temp0 = prey[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp4 = otherHunter[0] + temp3
	if dist > otherHunter[0] :
		if temp2 != 0:
			temp5 = temp2 / temp2
		else:
			temp5 = temp2
	else:
		if dist != 0:
			temp5 = otherHunter[1] / dist
		else:
			temp5 = dist
	temp6 = max( temp2 , temp5 )
	temp7 = max( temp4 , temp5 )
	temp1 = temp5 * prey[0]
	return [ temp3 , temp0 ]
