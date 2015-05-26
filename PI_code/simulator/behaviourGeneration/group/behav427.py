#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	if dist != 0:
		temp1 = otherHunter[1] / dist
	else:
		temp1 = dist
	if otherHunter[0] != 0:
		temp2 = otherHunter[0] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	if otherHunter[0] != 0:
		temp0 = prey[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if dist != 0:
		temp3 = prey[1] % dist
	else:
		temp3 = dist
	temp4 = otherHunter[1] + temp3
	return [ temp1 , prey[1] ]
