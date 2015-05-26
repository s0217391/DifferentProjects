#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , prey[1] )
	temp1 = dist + temp0
	temp0 = max( temp0 , temp1 )
	if prey[0] != 0:
		temp2 = dist / prey[0]
	else:
		temp2 = prey[0]
	if temp2 != 0:
		temp1 = otherHunter[1] / temp2
	else:
		temp1 = temp2
	temp3 = max( prey[0] , prey[1] )
	temp2 = max( prey[1] , temp0 )
	temp3 = min( temp0 , prey[0] )
	temp1 = -1 * temp3
	if prey[1] > prey[1] :
		temp2 = min( dist , temp2 )
	else:
		temp2 = temp1 + prey[1]
	temp1 = -1 * dist
	if temp2 > otherHunter[1] :
		temp3 = prey[0] * temp0
	else:
		temp3 = temp1 - temp3
	temp0 = temp3 + prey[1]
	temp3 = max( temp0 , otherHunter[1] )
	return [ dist , prey[0] ]
