#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - otherHunter[0]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp2 = max( otherHunter[0] , otherHunter[0] )
	temp2 = temp1 - prey[0]
	temp3 = max( prey[1] , prey[1] )
	if temp1 != 0:
		temp4 = otherHunter[0] % temp1
	else:
		temp4 = temp1
	temp2 = prey[0] - prey[1]
	if otherHunter[1] > otherHunter[0] :
		if temp2 > temp3 :
			if temp1 > otherHunter[1] :
				temp3 = max( temp2 , temp2 )
			else:
				temp3 = max( temp1 , dist )
		else:
			temp3 = otherHunter[1] - temp2
	else:
		temp3 = prey[0] * prey[1]
	temp0 = max( prey[1] , prey[1] )
	temp3 = min( dist , prey[1] )
	temp0 = max( temp2 , dist )
	if temp0 != 0:
		temp4 = otherHunter[0] % temp0
	else:
		temp4 = temp0
	temp2 = temp4 + otherHunter[0]
	temp2 = -1 * prey[1]
	temp0 = min( otherHunter[1] , dist )
	temp2 = otherHunter[1] * otherHunter[0]
	return [ prey[1] , otherHunter[0] ]
