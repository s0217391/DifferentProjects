#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	if otherHunter[1] != 0:
		temp1 = otherHunter[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp0 = otherHunter[1] + dist
	temp1 = min( otherHunter[0] , dist )
	temp1 = temp1 - temp0
	if otherHunter[0] != 0:
		temp2 = otherHunter[1] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp3 = prey[1] + prey[0]
	return [ dist , prey[1] ]
