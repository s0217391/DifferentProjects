#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if otherHunter[0] != 0:
		temp1 = temp0 % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if otherHunter[1] != 0:
		temp2 = otherHunter[0] % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp1 = -1 * temp1
	if otherHunter[1] != 0:
		temp0 = prey[1] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	return [ otherHunter[0] , dist ]
