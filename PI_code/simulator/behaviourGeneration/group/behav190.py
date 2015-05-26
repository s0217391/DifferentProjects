#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = max( otherHunter[1] , prey[1] )
	temp1 = otherHunter[0] + otherHunter[1]
	temp2 = otherHunter[0] * otherHunter[1]
	temp0 = max( otherHunter[0] , temp0 )
	temp2 = prey[1] + otherHunter[0]
	temp0 = -1 * prey[0]
	temp2 = max( prey[0] , temp0 )
	if dist > temp0 :
		temp1 = -1 * otherHunter[1]
	else:
		temp1 = -1 * temp0
	if otherHunter[0] > prey[1] :
		if temp1 > otherHunter[0] :
			temp3 = prey[1] * temp0
		else:
			temp3 = -1 * temp0
	else:
		if temp1 != 0:
			temp3 = prey[1] % temp1
		else:
			temp3 = temp1
	temp0 = min( temp0 , temp0 )
	if temp2 != 0:
		temp3 = temp3 % temp2
	else:
		temp3 = temp2
	if temp3 != 0:
		temp1 = prey[1] / temp3
	else:
		temp1 = temp3
	temp4 = max( temp1 , temp2 )
	return [ otherHunter[0] , dist ]
