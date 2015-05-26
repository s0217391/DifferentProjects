#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * dist
	if otherHunter[0] != 0:
		temp1 = prey[1] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp1 = prey[1] + dist
	temp2 = -1 * prey[1]
	temp2 = prey[1] + otherHunter[1]
	return [ otherHunter[1] , dist ]
