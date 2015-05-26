#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * otherHunter[0]
	temp1 = -1 * otherHunter[1]
	temp2 = temp0 * temp1
	temp2 = otherHunter[0] + temp1
	temp0 = -1 * prey[0]
	temp1 = -1 * temp1
	if temp0 > prey[0] :
		temp3 = -1 * temp2
	else:
		if otherHunter[1] != 0:
			temp3 = temp1 / otherHunter[1]
		else:
			temp3 = otherHunter[1]
	temp4 = min( temp1 , otherHunter[0] )
	if prey[1] > temp2 :
		if prey[1] != 0:
			temp4 = temp4 / prey[1]
		else:
			temp4 = prey[1]
	else:
		temp4 = temp4 + otherHunter[0]
	temp4 = temp2 - dist
	return [ otherHunter[1] , temp0 ]
