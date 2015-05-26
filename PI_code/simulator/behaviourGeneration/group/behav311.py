#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - prey[1]
	temp1 = max( prey[1] , dist )
	temp2 = dist - prey[0]
	if temp2 != 0:
		temp0 = dist % temp2
	else:
		temp0 = temp2
	if otherHunter[0] != 0:
		temp1 = prey[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = temp1 + temp2
	temp2 = min( otherHunter[0] , otherHunter[1] )
	temp1 = max( dist , temp2 )
	temp2 = dist - otherHunter[1]
	if temp2 > temp1 :
		if prey[0] != 0:
			temp0 = dist / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = max( temp0 , temp0 )
	if prey[1] != 0:
		temp3 = otherHunter[1] % prey[1]
	else:
		temp3 = prey[1]
	temp0 = prey[1] - temp1
	temp2 = max( prey[0] , temp3 )
	temp3 = otherHunter[0] * temp1
	temp3 = min( prey[1] , dist )
	return [ dist , temp0 ]
