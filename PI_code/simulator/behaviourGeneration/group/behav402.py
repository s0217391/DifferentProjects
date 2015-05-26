#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , prey[1] )
	temp1 = -1 * dist
	temp2 = temp0 - dist
	temp2 = max( temp0 , temp2 )
	if dist != 0:
		temp1 = dist / dist
	else:
		temp1 = dist
	temp0 = max( otherHunter[0] , temp2 )
	if temp1 > otherHunter[0] :
		temp2 = temp1 * dist
	else:
		temp2 = min( temp0 , prey[0] )
	temp1 = dist + temp2
	temp3 = temp0 * dist
	temp4 = min( temp3 , prey[0] )
	temp3 = temp1 - temp3
	temp4 = temp3 + prey[0]
	temp1 = prey[0] - temp2
	temp0 = temp3 + temp4
	return [ temp4 , temp4 ]
