#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = dist / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = min( otherHunter[0] , otherHunter[1] )
	temp2 = otherHunter[1] - prey[1]
	temp1 = dist + temp2
	temp2 = min( prey[1] , prey[0] )
	if prey[1] != 0:
		temp0 = temp0 % prey[1]
	else:
		temp0 = prey[1]
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	if otherHunter[0] != 0:
		temp2 = prey[1] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp1 = max( temp2 , temp1 )
	temp1 = temp2 + dist
	if prey[1] > prey[0] :
		if otherHunter[0] != 0:
			temp0 = prey[1] / otherHunter[0]
		else:
			temp0 = otherHunter[0]
	else:
		temp0 = prey[1] + temp0
	if prey[1] != 0:
		temp2 = temp1 % prey[1]
	else:
		temp2 = prey[1]
	if prey[0] != 0:
		temp0 = otherHunter[1] / prey[0]
	else:
		temp0 = prey[0]
	temp0 = dist - temp0
	if prey[0] != 0:
		temp3 = temp2 / prey[0]
	else:
		temp3 = prey[0]
	temp4 = prey[1] * temp1
	if dist != 0:
		temp5 = temp2 / dist
	else:
		temp5 = dist
	temp1 = temp2 * prey[1]
	temp6 = otherHunter[1] - temp5
	temp4 = dist - temp2
	temp3 = dist * temp1
	if prey[1] != 0:
		temp0 = temp0 % prey[1]
	else:
		temp0 = prey[1]
	temp6 = min( temp1 , prey[0] )
	temp7 = temp5 + otherHunter[1]
	temp3 = prey[1] - dist
	return [ temp6 , temp0 ]
