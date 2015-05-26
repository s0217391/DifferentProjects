#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > otherHunter[0] :
		temp0 = otherHunter[1] * dist
	else:
		temp0 = prey[1] - otherHunter[0]
	temp1 = -1 * temp0
	if prey[1] > otherHunter[1] :
		temp1 = min( otherHunter[0] , dist )
	else:
		if dist != 0:
			temp1 = dist / dist
		else:
			temp1 = dist
	temp0 = temp1 * temp0
	temp0 = -1 * dist
	temp1 = min( otherHunter[1] , otherHunter[1] )
	temp1 = prey[1] - dist
	temp0 = temp1 * temp0
	temp1 = min( temp0 , temp1 )
	temp1 = max( otherHunter[0] , temp1 )
	temp0 = temp0 + prey[0]
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp0 = min( prey[0] , temp0 )
	temp2 = otherHunter[1] + temp0
	temp3 = otherHunter[0] - prey[1]
	return [ prey[1] , temp1 ]
