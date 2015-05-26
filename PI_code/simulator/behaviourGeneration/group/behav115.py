#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + prey[1]
	temp1 = -1 * prey[1]
	if otherHunter[0] > temp1 :
		temp0 = -1 * prey[0]
	else:
		if otherHunter[0] != 0:
			temp0 = temp1 % otherHunter[0]
		else:
			temp0 = otherHunter[0]
	temp2 = -1 * prey[1]
	if otherHunter[0] > temp2 :
		temp3 = -1 * prey[0]
	else:
		temp3 = dist - otherHunter[0]
	temp4 = max( prey[1] , otherHunter[1] )
	temp1 = prey[0] + otherHunter[0]
	if prey[1] != 0:
		temp3 = prey[0] % prey[1]
	else:
		temp3 = prey[1]
	return [ otherHunter[0] , prey[0] ]
