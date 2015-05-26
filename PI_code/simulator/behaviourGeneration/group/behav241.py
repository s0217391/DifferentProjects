#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + prey[1]
	if otherHunter[0] != 0:
		temp1 = dist / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if dist > otherHunter[1] :
		temp1 = otherHunter[0] * temp1
	else:
		temp1 = max( temp0 , otherHunter[0] )
	if prey[0] != 0:
		temp2 = otherHunter[0] % prey[0]
	else:
		temp2 = prey[0]
	temp2 = min( prey[0] , temp0 )
	temp3 = prey[1] + prey[0]
	temp1 = max( prey[1] , otherHunter[0] )
	temp2 = otherHunter[1] - temp0
	temp2 = -1 * temp0
	if temp2 != 0:
		temp4 = temp3 % temp2
	else:
		temp4 = temp2
	temp1 = max( prey[0] , otherHunter[0] )
	if otherHunter[0] != 0:
		temp2 = temp1 % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp1 = -1 * otherHunter[1]
	temp1 = -1 * temp3
	temp5 = min( temp2 , otherHunter[0] )
	temp5 = temp2 + otherHunter[0]
	temp5 = min( otherHunter[1] , temp4 )
	temp0 = -1 * temp2
	if prey[1] != 0:
		temp1 = temp2 % prey[1]
	else:
		temp1 = prey[1]
	if temp2 > otherHunter[1] :
		temp1 = temp5 + otherHunter[0]
	else:
		temp1 = -1 * prey[1]
	temp3 = max( temp2 , otherHunter[0] )
	temp4 = min( temp4 , prey[1] )
	return [ temp2 , prey[1] ]
