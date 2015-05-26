#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * dist
	if dist != 0:
		temp1 = prey[1] % dist
	else:
		temp1 = dist
	temp0 = max( temp1 , prey[1] )
	if prey[1] != 0:
		temp2 = temp1 / prey[1]
	else:
		temp2 = prey[1]
	temp0 = otherHunter[1] * otherHunter[0]
	if prey[0] != 0:
		temp2 = dist % prey[0]
	else:
		temp2 = prey[0]
	if dist != 0:
		temp0 = prey[0] / dist
	else:
		temp0 = dist
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if dist != 0:
		temp2 = otherHunter[0] % dist
	else:
		temp2 = dist
	temp2 = otherHunter[0] * prey[1]
	temp3 = otherHunter[0] - otherHunter[0]
	return [ temp1 , prey[0] ]
