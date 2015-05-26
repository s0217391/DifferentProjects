#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + dist
	if otherHunter[1] != 0:
		temp1 = dist / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = temp1 * temp0
	if prey[0] > otherHunter[0] :
		if otherHunter[1] != 0:
			temp2 = dist % otherHunter[1]
		else:
			temp2 = otherHunter[1]
	else:
		temp2 = prey[0] + prey[1]
	temp2 = -1 * dist
	temp0 = min( temp1 , temp2 )
	if dist != 0:
		temp0 = dist % dist
	else:
		temp0 = dist
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp1 = dist + prey[0]
	temp0 = max( dist , otherHunter[0] )
	if dist != 0:
		temp0 = prey[0] % dist
	else:
		temp0 = dist
	if temp1 != 0:
		temp1 = otherHunter[0] / temp1
	else:
		temp1 = temp1
	temp0 = -1 * temp1
	temp2 = -1 * otherHunter[0]
	temp2 = -1 * temp1
	temp2 = otherHunter[0] - otherHunter[0]
	temp2 = temp1 + otherHunter[1]
	return [ temp2 , temp1 ]
