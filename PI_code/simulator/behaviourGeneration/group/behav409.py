#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , otherHunter[0] )
	temp1 = otherHunter[1] * dist
	if dist != 0:
		temp2 = temp1 % dist
	else:
		temp2 = dist
	temp0 = dist - prey[0]
	temp1 = max( temp1 , prey[0] )
	temp2 = otherHunter[0] + temp1
	temp3 = max( dist , temp0 )
	temp1 = max( prey[0] , temp1 )
	temp0 = prey[0] + otherHunter[0]
	temp2 = temp0 + temp2
	temp0 = -1 * dist
	if prey[0] != 0:
		temp0 = temp3 % prey[0]
	else:
		temp0 = prey[0]
	temp0 = -1 * temp1
	temp3 = min( prey[0] , temp2 )
	temp3 = prey[0] - otherHunter[0]
	temp3 = dist - temp1
	temp1 = temp0 + temp3
	temp2 = max( temp0 , temp1 )
	temp3 = temp3 * dist
	if temp3 > prey[1] :
		temp2 = min( dist , otherHunter[0] )
	else:
		if temp1 > temp2 :
			if prey[0] != 0:
				temp2 = temp1 / prey[0]
			else:
				temp2 = prey[0]
		else:
			temp2 = temp0 * otherHunter[0]
	temp3 = min( prey[0] , prey[1] )
	return [ temp0 , temp2 ]
