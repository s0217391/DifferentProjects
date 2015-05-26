#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , prey[1] )
	if otherHunter[1] != 0:
		temp1 = prey[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[0] != 0:
		temp0 = otherHunter[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[1] - temp0
	temp0 = prey[0] * otherHunter[0]
	temp2 = otherHunter[1] * prey[0]
	if prey[1] > otherHunter[0] :
		temp0 = max( temp2 , otherHunter[1] )
	else:
		temp0 = prey[0] + dist
	temp3 = otherHunter[1] - otherHunter[0]
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	temp1 = otherHunter[1] * prey[1]
	temp0 = min( temp3 , dist )
	temp1 = -1 * dist
	temp2 = max( temp1 , prey[1] )
	temp0 = -1 * otherHunter[0]
	temp3 = max( otherHunter[0] , otherHunter[0] )
	temp3 = -1 * temp0
	if otherHunter[0] > otherHunter[0] :
		if temp1 != 0:
			temp2 = otherHunter[1] % temp1
		else:
			temp2 = temp1
	else:
		temp2 = dist * temp0
	if otherHunter[1] != 0:
		temp0 = temp0 / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = prey[0] - temp1
	temp1 = prey[0] + temp3
	if temp3 != 0:
		temp1 = temp2 % temp3
	else:
		temp1 = temp3
	temp2 = -1 * prey[1]
	temp3 = -1 * dist
	if dist > dist :
		temp3 = otherHunter[1] - otherHunter[1]
	else:
		temp3 = temp2 - prey[0]
	temp1 = max( otherHunter[1] , temp0 )
	return [ temp3 , prey[1] ]
