#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = otherHunter[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = max( otherHunter[0] , temp0 )
	if otherHunter[0] != 0:
		temp1 = otherHunter[1] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if otherHunter[0] > temp0 :
		if prey[0] > prey[0] :
			temp0 = dist + dist
		else:
			temp0 = dist - dist
	else:
		temp0 = max( prey[1] , prey[1] )
	temp1 = -1 * temp1
	if prey[1] > temp0 :
		if dist != 0:
			temp2 = otherHunter[0] / dist
		else:
			temp2 = dist
	else:
		temp2 = -1 * temp0
	temp3 = dist - temp0
	temp3 = temp0 - temp2
	temp3 = prey[0] - otherHunter[1]
	temp3 = temp3 * temp2
	return [ otherHunter[0] , prey[1] ]
