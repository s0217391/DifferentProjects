#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if prey[1] > otherHunter[0] :
		temp1 = prey[0] + dist
	else:
		temp1 = -1 * temp0
	temp2 = prey[1] - dist
	temp2 = max( temp1 , otherHunter[1] )
	temp0 = prey[0] - temp0
	temp0 = temp2 - temp0
	if otherHunter[1] != 0:
		temp2 = otherHunter[0] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if otherHunter[1] != 0:
		temp0 = dist % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = prey[0] * prey[0]
	temp0 = otherHunter[0] - prey[0]
	if prey[0] > prey[0] :
		temp2 = -1 * prey[0]
	else:
		temp2 = dist + otherHunter[1]
	temp1 = dist - temp1
	temp2 = temp2 + temp2
	if otherHunter[0] != 0:
		temp2 = prey[0] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	if otherHunter[0] > otherHunter[0] :
		temp3 = temp1 - temp2
	else:
		if temp1 != 0:
			temp3 = temp1 % temp1
		else:
			temp3 = temp1
	if prey[1] != 0:
		temp3 = prey[0] % prey[1]
	else:
		temp3 = prey[1]
	temp1 = min( temp2 , temp3 )
	temp2 = temp2 + dist
	return [ dist , temp1 ]
