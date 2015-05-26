#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , prey[0] )
	temp1 = temp0 - prey[0]
	temp2 = min( dist , prey[0] )
	if prey[0] != 0:
		temp3 = temp2 / prey[0]
	else:
		temp3 = prey[0]
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp4 = temp1 - otherHunter[0]
	temp4 = min( temp2 , temp1 )
	if temp0 > otherHunter[0] :
		temp1 = max( temp1 , temp3 )
	else:
		if prey[1] > prey[0] :
			if temp0 != 0:
				temp1 = otherHunter[1] % temp0
			else:
				temp1 = temp0
		else:
			temp1 = temp1 - otherHunter[1]
	temp0 = min( temp1 , prey[1] )
	if otherHunter[0] > otherHunter[0] :
		temp3 = prey[1] + temp1
	else:
		if otherHunter[0] > otherHunter[0] :
			temp3 = temp0 + temp3
		else:
			temp3 = max( otherHunter[0] , temp0 )
	temp5 = prey[0] + temp4
	if prey[0] != 0:
		temp3 = temp3 / prey[0]
	else:
		temp3 = prey[0]
	return [ temp0 , otherHunter[0] ]
