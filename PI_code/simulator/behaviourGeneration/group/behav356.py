#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = otherHunter[0] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = otherHunter[1] + otherHunter[0]
	if temp0 > temp1 :
		temp1 = min( otherHunter[0] , otherHunter[1] )
	else:
		temp1 = dist + temp1
	temp1 = -1 * prey[0]
	if prey[1] != 0:
		temp1 = otherHunter[0] % prey[1]
	else:
		temp1 = prey[1]
	temp0 = temp0 * dist
	return [ otherHunter[1] , otherHunter[0] ]
