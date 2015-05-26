#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , otherHunter[1] )
	temp1 = otherHunter[0] + prey[1]
	if otherHunter[1] > prey[0] :
		temp2 = min( otherHunter[0] , prey[1] )
	else:
		temp2 = prey[1] * dist
	temp3 = -1 * dist
	if prey[1] > prey[1] :
		temp1 = otherHunter[0] + otherHunter[0]
	else:
		if temp0 > temp1 :
			temp1 = min( temp0 , temp2 )
		else:
			if otherHunter[1] != 0:
				temp1 = temp1 % otherHunter[1]
			else:
				temp1 = otherHunter[1]
	temp1 = -1 * prey[1]
	if temp2 != 0:
		temp0 = dist % temp2
	else:
		temp0 = temp2
	if otherHunter[1] != 0:
		temp3 = temp1 / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	if temp3 > otherHunter[1] :
		temp2 = -1 * temp1
	else:
		temp2 = min( prey[0] , temp3 )
	temp0 = min( prey[0] , dist )
	return [ temp3 , prey[0] ]
