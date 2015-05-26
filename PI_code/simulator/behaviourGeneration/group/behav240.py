#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > prey[1] :
		temp0 = prey[0] + prey[1]
	else:
		if dist != 0:
			temp0 = prey[1] / dist
		else:
			temp0 = dist
	if otherHunter[1] > temp0 :
		if dist != 0:
			temp1 = temp0 % dist
		else:
			temp1 = dist
	else:
		temp1 = prey[1] + otherHunter[1]
	temp0 = prey[1] * dist
	if temp0 > prey[1] :
		if prey[1] != 0:
			temp2 = temp0 / prey[1]
		else:
			temp2 = prey[1]
	else:
		temp2 = max( prey[1] , temp0 )
	temp1 = dist + otherHunter[1]
	return [ prey[1] , prey[0] ]
