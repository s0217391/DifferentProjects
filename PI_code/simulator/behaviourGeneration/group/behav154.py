#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + dist
	if temp0 != 0:
		temp1 = dist / temp0
	else:
		temp1 = temp0
	temp1 = temp0 * temp1
	temp2 = min( otherHunter[1] , prey[1] )
	temp0 = min( otherHunter[0] , temp2 )
	if prey[1] != 0:
		temp1 = dist / prey[1]
	else:
		temp1 = prey[1]
	temp2 = max( prey[1] , prey[1] )
	if temp2 != 0:
		temp2 = temp0 % temp2
	else:
		temp2 = temp2
	temp1 = min( temp2 , otherHunter[1] )
	temp1 = dist * temp0
	temp2 = prey[0] - dist
	temp0 = min( temp1 , temp1 )
	temp0 = min( otherHunter[1] , prey[1] )
	if temp0 != 0:
		temp2 = temp0 / temp0
	else:
		temp2 = temp0
	temp0 = min( temp2 , temp2 )
	if temp0 > temp0 :
		temp3 = prey[0] + dist
	else:
		temp3 = temp0 + temp0
	temp3 = temp2 * temp0
	temp0 = min( temp0 , temp1 )
	if prey[1] != 0:
		temp3 = prey[1] % prey[1]
	else:
		temp3 = prey[1]
	temp4 = max( temp2 , temp0 )
	temp1 = max( prey[1] , temp0 )
	temp0 = min( dist , otherHunter[1] )
	temp2 = temp1 - temp1
	temp5 = otherHunter[0] * temp0
	temp6 = -1 * otherHunter[0]
	return [ prey[0] , temp0 ]
