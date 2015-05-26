#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > otherHunter[1] :
		if otherHunter[0] != 0:
			temp0 = prey[0] % otherHunter[0]
		else:
			temp0 = otherHunter[0]
	else:
		temp0 = -1 * prey[1]
	if prey[0] != 0:
		temp1 = prey[1] % prey[0]
	else:
		temp1 = prey[0]
	if otherHunter[1] != 0:
		temp0 = otherHunter[1] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	temp2 = otherHunter[0] - otherHunter[1]
	if temp2 > dist :
		temp0 = min( prey[0] , dist )
	else:
		temp0 = dist * temp0
	temp0 = -1 * temp1
	temp1 = prey[1] + temp0
	temp3 = prey[0] * temp2
	temp4 = -1 * temp1
	return [ prey[0] , prey[1] ]
