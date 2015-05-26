#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = dist % prey[0]
	else:
		temp0 = prey[0]
	if dist > otherHunter[0] :
		if otherHunter[0] != 0:
			temp1 = prey[1] % otherHunter[0]
		else:
			temp1 = otherHunter[0]
	else:
		if otherHunter[0] > otherHunter[1] :
			if temp0 != 0:
				temp1 = otherHunter[0] / temp0
			else:
				temp1 = temp0
		else:
			temp1 = max( otherHunter[0] , dist )
	if otherHunter[1] > otherHunter[1] :
		if otherHunter[0] != 0:
			temp0 = prey[1] % otherHunter[0]
		else:
			temp0 = otherHunter[0]
	else:
		temp0 = min( temp1 , otherHunter[1] )
	return [ otherHunter[1] , otherHunter[0] ]
