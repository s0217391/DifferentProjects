#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , prey[0] )
	temp1 = max( prey[0] , prey[1] )
	if prey[1] != 0:
		temp0 = otherHunter[0] / prey[1]
	else:
		temp0 = prey[1]
	temp2 = min( prey[1] , dist )
	if prey[1] != 0:
		temp2 = temp0 / prey[1]
	else:
		temp2 = prey[1]
	temp3 = max( otherHunter[0] , dist )
	temp1 = min( temp3 , prey[1] )
	if prey[1] != 0:
		temp4 = dist / prey[1]
	else:
		temp4 = prey[1]
	if temp1 != 0:
		temp4 = temp1 / temp1
	else:
		temp4 = temp1
	if dist != 0:
		temp2 = temp4 / dist
	else:
		temp2 = dist
	temp3 = otherHunter[0] * temp0
	temp0 = max( temp3 , temp2 )
	if otherHunter[0] > temp2 :
		if temp0 > temp2 :
			temp3 = max( temp1 , dist )
		else:
			if temp0 != 0:
				temp3 = temp2 % temp0
			else:
				temp3 = temp0
	else:
		temp3 = max( otherHunter[1] , prey[0] )
	temp1 = otherHunter[0] - prey[1]
	if temp2 != 0:
		temp0 = temp3 / temp2
	else:
		temp0 = temp2
	temp2 = min( prey[1] , dist )
	temp4 = prey[0] + dist
	temp5 = max( otherHunter[0] , temp1 )
	if otherHunter[1] != 0:
		temp2 = temp0 / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	return [ dist , temp3 ]
