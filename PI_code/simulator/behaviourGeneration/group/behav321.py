#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = max( otherHunter[0] , otherHunter[1] )
	temp1 = temp1 - otherHunter[1]
	if dist != 0:
		temp2 = otherHunter[1] / dist
	else:
		temp2 = dist
	if otherHunter[1] > dist :
		if otherHunter[1] != 0:
			temp3 = prey[1] / otherHunter[1]
		else:
			temp3 = otherHunter[1]
	else:
		temp3 = -1 * temp2
	temp1 = min( otherHunter[0] , otherHunter[0] )
	if dist != 0:
		temp2 = temp3 % dist
	else:
		temp2 = dist
	if otherHunter[0] != 0:
		temp3 = otherHunter[1] % otherHunter[0]
	else:
		temp3 = otherHunter[0]
	if temp2 != 0:
		temp0 = temp2 / temp2
	else:
		temp0 = temp2
	temp1 = temp1 - temp2
	if otherHunter[1] != 0:
		temp1 = temp3 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	temp2 = prey[0] - prey[0]
	return [ temp0 , prey[0] ]
