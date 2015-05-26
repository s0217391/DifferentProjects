#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = prey[0] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if otherHunter[1] > otherHunter[1] :
		if dist > prey[1] :
			temp1 = dist - otherHunter[0]
		else:
			temp1 = otherHunter[0] - prey[1]
	else:
		if prey[0] != 0:
			temp1 = prey[1] / prey[0]
		else:
			temp1 = prey[0]
	temp1 = max( otherHunter[0] , prey[0] )
	temp0 = max( otherHunter[1] , otherHunter[1] )
	if dist > otherHunter[1] :
		if otherHunter[0] > prey[1] :
			temp1 = dist * temp1
		else:
			if temp0 != 0:
				temp1 = dist % temp0
			else:
				temp1 = temp0
	else:
		temp1 = max( temp1 , temp0 )
	temp2 = max( otherHunter[0] , otherHunter[0] )
	if otherHunter[1] != 0:
		temp2 = temp0 % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	return [ otherHunter[0] , otherHunter[1] ]
