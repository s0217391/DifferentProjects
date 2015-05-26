#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist * prey[1]
	temp1 = dist + prey[0]
	temp2 = min( otherHunter[0] , prey[0] )
	temp1 = otherHunter[0] - temp0
	temp1 = -1 * dist
	if temp2 > otherHunter[0] :
		if dist > prey[1] :
			if temp1 != 0:
				temp0 = temp0 % temp1
			else:
				temp0 = temp1
		else:
			temp0 = temp0 - otherHunter[0]
	else:
		temp0 = max( prey[1] , temp0 )
	temp1 = min( otherHunter[0] , temp1 )
	if temp0 != 0:
		temp2 = otherHunter[1] % temp0
	else:
		temp2 = temp0
	temp1 = min( prey[1] , temp2 )
	temp1 = temp1 * otherHunter[1]
	if otherHunter[0] > dist :
		if prey[0] != 0:
			temp3 = temp2 % prey[0]
		else:
			temp3 = prey[0]
	else:
		if prey[1] > dist :
			temp3 = min( otherHunter[1] , temp2 )
		else:
			temp3 = max( otherHunter[0] , otherHunter[0] )
	temp3 = dist * otherHunter[0]
	temp4 = temp2 * temp3
	temp0 = temp4 - temp3
	if temp4 != 0:
		temp3 = temp2 % temp4
	else:
		temp3 = temp4
	temp5 = dist - temp1
	temp5 = -1 * dist
	return [ temp2 , dist ]
