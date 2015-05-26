#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - dist
	if dist != 0:
		temp1 = prey[1] / dist
	else:
		temp1 = dist
	if otherHunter[1] > prey[1] :
		temp2 = temp1 * dist
	else:
		temp2 = min( temp0 , temp1 )
	temp1 = min( prey[1] , otherHunter[0] )
	temp2 = otherHunter[1] + dist
	temp1 = min( otherHunter[1] , temp1 )
	temp2 = prey[1] + prey[0]
	temp0 = max( prey[0] , temp1 )
	temp1 = max( dist , otherHunter[1] )
	if temp2 != 0:
		temp0 = otherHunter[1] / temp2
	else:
		temp0 = temp2
	if otherHunter[0] != 0:
		temp3 = temp2 / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	if temp3 != 0:
		temp1 = otherHunter[0] % temp3
	else:
		temp1 = temp3
	if otherHunter[1] != 0:
		temp1 = prey[0] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	temp4 = -1 * temp2
	if prey[0] != 0:
		temp4 = prey[0] % prey[0]
	else:
		temp4 = prey[0]
	temp5 = temp4 * otherHunter[0]
	temp0 = temp2 * temp5
	return [ temp5 , temp3 ]
