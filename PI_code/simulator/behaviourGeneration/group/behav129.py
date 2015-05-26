#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * prey[0]
	if dist != 0:
		temp1 = otherHunter[1] / dist
	else:
		temp1 = dist
	temp0 = temp0 - otherHunter[0]
	temp1 = otherHunter[0] - temp1
	temp0 = min( temp0 , otherHunter[1] )
	if dist != 0:
		temp0 = temp0 / dist
	else:
		temp0 = dist
	if otherHunter[0] != 0:
		temp1 = otherHunter[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = temp0 + prey[1]
	temp2 = -1 * temp0
	if temp1 != 0:
		temp1 = otherHunter[0] % temp1
	else:
		temp1 = temp1
	temp2 = -1 * prey[1]
	if prey[1] != 0:
		temp3 = prey[0] / prey[1]
	else:
		temp3 = prey[1]
	temp2 = -1 * otherHunter[0]
	temp1 = prey[1] + temp2
	if temp0 != 0:
		temp0 = temp0 / temp0
	else:
		temp0 = temp0
	if prey[0] != 0:
		temp4 = prey[0] % prey[0]
	else:
		temp4 = prey[0]
	if temp2 != 0:
		temp3 = temp3 / temp2
	else:
		temp3 = temp2
	if temp3 != 0:
		temp0 = dist % temp3
	else:
		temp0 = temp3
	if temp3 != 0:
		temp4 = prey[1] % temp3
	else:
		temp4 = temp3
	if temp4 != 0:
		temp3 = temp2 / temp4
	else:
		temp3 = temp4
	if prey[1] != 0:
		temp1 = otherHunter[1] % prey[1]
	else:
		temp1 = prey[1]
	temp1 = prey[1] - dist
	temp0 = temp0 * temp1
	temp3 = dist * otherHunter[1]
	return [ otherHunter[0] , temp1 ]
