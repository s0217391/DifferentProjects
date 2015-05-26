#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * prey[1]
	temp1 = prey[0] * otherHunter[0]
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	temp2 = temp0 - dist
	temp0 = max( dist , temp0 )
	temp0 = min( temp2 , temp1 )
	temp1 = min( otherHunter[0] , temp2 )
	if otherHunter[1] != 0:
		temp2 = prey[1] % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp0 = -1 * prey[0]
	if prey[0] != 0:
		temp2 = otherHunter[0] / prey[0]
	else:
		temp2 = prey[0]
	temp2 = prey[1] + temp0
	if temp1 != 0:
		temp1 = temp0 / temp1
	else:
		temp1 = temp1
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	return [ temp1 , dist ]
