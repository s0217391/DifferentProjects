#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = max( prey[1] , prey[0] )
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	temp2 = min( otherHunter[0] , prey[0] )
	temp1 = prey[1] - prey[1]
	temp1 = dist * prey[0]
	temp2 = min( temp1 , otherHunter[1] )
	if otherHunter[0] > temp2 :
		temp1 = min( prey[0] , temp2 )
	else:
		if temp0 != 0:
			temp1 = prey[0] % temp0
		else:
			temp1 = temp0
	if otherHunter[1] != 0:
		temp1 = prey[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp3 = min( prey[0] , dist )
	if prey[0] != 0:
		temp3 = prey[1] % prey[0]
	else:
		temp3 = prey[0]
	if dist != 0:
		temp0 = otherHunter[0] % dist
	else:
		temp0 = dist
	if prey[0] != 0:
		temp2 = temp0 % prey[0]
	else:
		temp2 = prey[0]
	temp0 = -1 * temp0
	temp1 = otherHunter[1] - temp2
	temp4 = -1 * otherHunter[1]
	if temp1 > otherHunter[1] :
		temp3 = prey[1] + temp4
	else:
		temp3 = temp0 + dist
	temp1 = otherHunter[0] - otherHunter[0]
	if prey[1] != 0:
		temp3 = otherHunter[1] % prey[1]
	else:
		temp3 = prey[1]
	if otherHunter[1] != 0:
		temp0 = otherHunter[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = -1 * temp2
	temp5 = min( temp1 , otherHunter[1] )
	temp4 = otherHunter[0] + temp4
	temp4 = temp3 - prey[1]
	temp2 = temp4 + temp1
	return [ prey[0] , temp0 ]
