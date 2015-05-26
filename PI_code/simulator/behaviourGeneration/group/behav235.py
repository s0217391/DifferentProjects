#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[0] :
		temp0 = -1 * dist
	else:
		temp0 = min( dist , prey[1] )
	if otherHunter[0] != 0:
		temp1 = prey[1] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = min( dist , temp0 )
	temp0 = otherHunter[1] * dist
	temp2 = temp1 * dist
	temp2 = temp2 * prey[0]
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp2 = temp0 - prey[0]
	temp0 = dist * temp2
	temp0 = prey[0] + temp1
	return [ temp1 , temp1 ]
