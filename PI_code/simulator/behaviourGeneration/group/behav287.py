#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist * otherHunter[1]
	temp1 = max( dist , prey[0] )
	temp2 = -1 * prey[1]
	if temp1 != 0:
		temp0 = prey[0] / temp1
	else:
		temp0 = temp1
	temp2 = dist + temp1
	if otherHunter[1] != 0:
		temp3 = otherHunter[0] / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp2 = -1 * temp2
	temp3 = min( otherHunter[0] , temp1 )
	if prey[0] > dist :
		temp0 = otherHunter[0] - otherHunter[0]
	else:
		temp0 = prey[0] * prey[0]
	temp4 = -1 * prey[0]
	if otherHunter[0] > temp2 :
		if otherHunter[1] > temp1 :
			if prey[1] != 0:
				temp1 = temp4 % prey[1]
			else:
				temp1 = prey[1]
		else:
			temp1 = -1 * temp3
	else:
		temp1 = dist - dist
	temp1 = dist - prey[1]
	if temp0 != 0:
		temp3 = temp1 % temp0
	else:
		temp3 = temp0
	if prey[1] != 0:
		temp0 = otherHunter[1] / prey[1]
	else:
		temp0 = prey[1]
	return [ temp1 , otherHunter[0] ]
