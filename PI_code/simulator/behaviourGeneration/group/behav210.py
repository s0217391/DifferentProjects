#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + prey[1]
	temp1 = min( temp0 , prey[1] )
	temp0 = max( prey[0] , otherHunter[1] )
	if prey[1] != 0:
		temp1 = dist / prey[1]
	else:
		temp1 = prey[1]
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	if temp0 != 0:
		temp1 = otherHunter[1] % temp0
	else:
		temp1 = temp0
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	temp1 = temp0 - prey[0]
	temp0 = temp1 * otherHunter[1]
	temp1 = min( temp0 , temp0 )
	temp0 = otherHunter[0] + prey[1]
	temp0 = max( dist , prey[0] )
	temp2 = otherHunter[0] + prey[1]
	temp1 = -1 * dist
	if temp0 > otherHunter[0] :
		temp0 = max( temp0 , prey[0] )
	else:
		temp0 = prey[0] * otherHunter[1]
	return [ dist , prey[1] ]