#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > otherHunter[1] :
		if otherHunter[1] > otherHunter[0] :
			temp0 = prey[1] * prey[1]
		else:
			if otherHunter[0] != 0:
				temp0 = otherHunter[0] / otherHunter[0]
			else:
				temp0 = otherHunter[0]
	else:
		if prey[1] != 0:
			temp0 = prey[0] / prey[1]
		else:
			temp0 = prey[1]
	temp1 = -1 * prey[1]
	if temp0 != 0:
		temp1 = dist % temp0
	else:
		temp1 = temp0
	temp0 = temp1 + otherHunter[0]
	if prey[1] > temp0 :
		temp0 = prey[0] + temp1
	else:
		if temp0 != 0:
			temp0 = otherHunter[1] % temp0
		else:
			temp0 = temp0
	if dist > prey[1] :
		temp1 = -1 * otherHunter[1]
	else:
		temp1 = max( temp1 , temp1 )
	return [ temp0 , otherHunter[1] ]
