#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + otherHunter[1]
	temp1 = dist * otherHunter[0]
	temp0 = -1 * temp0
	temp0 = temp1 - prey[1]
	temp2 = dist * temp0
	temp1 = -1 * otherHunter[1]
	temp2 = dist - prey[1]
	temp3 = prey[0] - temp1
	return [ prey[0] , prey[0] ]
