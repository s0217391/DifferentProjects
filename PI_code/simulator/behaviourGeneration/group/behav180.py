#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - prey[0]
	temp1 = otherHunter[1] + temp0
	temp0 = max( prey[0] , dist )
	temp1 = temp0 - otherHunter[0]
	if dist != 0:
		temp0 = prey[0] % dist
	else:
		temp0 = dist
	temp2 = prey[0] + temp0
	temp2 = temp2 - prey[1]
	if otherHunter[1] != 0:
		temp2 = otherHunter[1] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp2 = max( temp1 , temp1 )
	temp3 = temp2 - prey[0]
	temp4 = -1 * temp2
	temp1 = min( temp0 , temp1 )
	if prey[1] != 0:
		temp2 = prey[1] % prey[1]
	else:
		temp2 = prey[1]
	if prey[1] != 0:
		temp3 = prey[1] % prey[1]
	else:
		temp3 = prey[1]
	if prey[0] != 0:
		temp3 = otherHunter[1] / prey[0]
	else:
		temp3 = prey[0]
	temp1 = otherHunter[0] + otherHunter[1]
	temp4 = temp2 + otherHunter[0]
	temp3 = temp3 * temp1
	if temp1 != 0:
		temp1 = otherHunter[1] / temp1
	else:
		temp1 = temp1
	if temp0 != 0:
		temp3 = temp0 % temp0
	else:
		temp3 = temp0
	temp3 = -1 * temp0
	temp5 = temp1 - prey[1]
	if temp0 != 0:
		temp5 = temp0 / temp0
	else:
		temp5 = temp0
	return [ temp4 , temp2 ]
