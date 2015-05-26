#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	if otherHunter[1] != 0:
		temp1 = prey[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = temp0 * temp1
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	temp2 = prey[1] - prey[0]
	temp3 = min( prey[1] , prey[0] )
	temp4 = otherHunter[1] - temp1
	if temp4 > prey[0] :
		temp5 = min( temp1 , prey[0] )
	else:
		if prey[1] > temp0 :
			temp5 = otherHunter[1] * prey[1]
		else:
			if temp2 != 0:
				temp5 = temp2 % temp2
			else:
				temp5 = temp2
	temp1 = max( otherHunter[1] , temp4 )
	if temp3 != 0:
		temp2 = otherHunter[1] / temp3
	else:
		temp2 = temp3
	return [ temp0 , temp5 ]
