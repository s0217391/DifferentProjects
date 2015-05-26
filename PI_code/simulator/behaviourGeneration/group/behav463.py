#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + prey[1]
	temp1 = dist + dist
	if temp0 != 0:
		temp0 = otherHunter[0] % temp0
	else:
		temp0 = temp0
	temp0 = min( temp1 , temp0 )
	if otherHunter[0] != 0:
		temp1 = prey[1] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = prey[0] - prey[1]
	temp1 = otherHunter[0] * prey[1]
	temp0 = min( otherHunter[1] , dist )
	temp2 = otherHunter[1] + temp1
	if otherHunter[0] > prey[1] :
		if dist != 0:
			temp0 = prey[1] % dist
		else:
			temp0 = dist
	else:
		if temp2 != 0:
			temp0 = temp2 % temp2
		else:
			temp0 = temp2
	temp0 = otherHunter[0] - temp0
	temp0 = prey[0] * otherHunter[0]
	temp3 = min( temp1 , prey[1] )
	temp2 = otherHunter[0] - temp3
	temp4 = min( temp3 , temp0 )
	temp5 = min( temp0 , temp1 )
	return [ prey[0] , temp2 ]
