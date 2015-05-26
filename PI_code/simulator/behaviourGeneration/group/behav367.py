#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = prey[0] - prey[0]
	temp2 = prey[1] - prey[0]
	temp0 = otherHunter[0] * temp2
	return [ temp1 , temp1 ]
