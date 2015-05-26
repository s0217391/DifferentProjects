#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , prey[1] )
	temp1 = min( prey[0] , prey[0] )
	temp0 = prey[0] - temp0
	if prey[1] != 0:
		temp1 = dist / prey[1]
	else:
		temp1 = prey[1]
	temp0 = temp1 + otherHunter[1]
	if temp1 != 0:
		temp0 = temp0 / temp1
	else:
		temp0 = temp1
	if prey[1] != 0:
		temp2 = prey[1] % prey[1]
	else:
		temp2 = prey[1]
	if otherHunter[1] > dist :
		temp3 = -1 * otherHunter[0]
	else:
		if temp0 != 0:
			temp3 = temp0 % temp0
		else:
			temp3 = temp0
	temp3 = max( dist , prey[1] )
	temp0 = otherHunter[1] - otherHunter[1]
	if temp3 != 0:
		temp1 = temp0 % temp3
	else:
		temp1 = temp3
	temp0 = min( prey[1] , prey[1] )
	temp2 = temp3 - temp2
	if temp1 != 0:
		temp0 = temp0 % temp1
	else:
		temp0 = temp1
	if temp0 > otherHunter[0] :
		if temp3 > prey[0] :
			temp0 = -1 * temp1
		else:
			temp0 = otherHunter[1] - temp3
	else:
		temp0 = min( temp2 , temp1 )
	return [ temp1 , otherHunter[1] ]
