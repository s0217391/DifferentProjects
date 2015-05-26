#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[1] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = min( prey[1] , otherHunter[0] )
	temp2 = -1 * prey[0]
	if otherHunter[0] != 0:
		temp2 = prey[0] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	if temp1 != 0:
		temp3 = prey[0] % temp1
	else:
		temp3 = temp1
	temp0 = otherHunter[0] - dist
	temp0 = min( temp1 , temp3 )
	temp1 = -1 * temp3
	if temp3 > otherHunter[1] :
		temp2 = temp3 + prey[1]
	else:
		temp2 = min( temp1 , prey[1] )
	temp4 = min( prey[1] , prey[0] )
	if otherHunter[0] != 0:
		temp3 = temp4 / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp1 = min( prey[0] , prey[0] )
	temp2 = otherHunter[1] - temp3
	return [ prey[1] , otherHunter[1] ]
