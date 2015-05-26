#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = prey[1] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if prey[0] != 0:
		temp1 = otherHunter[1] / prey[0]
	else:
		temp1 = prey[0]
	if otherHunter[0] > prey[0] :
		if dist > otherHunter[1] :
			temp1 = dist - prey[1]
		else:
			if prey[0] != 0:
				temp1 = dist % prey[0]
			else:
				temp1 = prey[0]
	else:
		temp1 = max( otherHunter[1] , temp1 )
	temp0 = otherHunter[1] - dist
	if temp0 != 0:
		temp1 = otherHunter[1] % temp0
	else:
		temp1 = temp0
	temp2 = max( temp1 , otherHunter[0] )
	return [ dist , dist ]
