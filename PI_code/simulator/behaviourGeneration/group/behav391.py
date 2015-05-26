#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + dist
	temp1 = dist + otherHunter[1]
	temp0 = otherHunter[1] + otherHunter[0]
	temp0 = prey[1] - dist
	if dist > prey[1] :
		if temp0 != 0:
			temp2 = dist / temp0
		else:
			temp2 = temp0
	else:
		temp2 = otherHunter[0] + temp0
	if prey[1] != 0:
		temp2 = temp1 / prey[1]
	else:
		temp2 = prey[1]
	temp3 = min( otherHunter[1] , dist )
	temp1 = min( temp2 , temp3 )
	temp1 = min( temp1 , temp1 )
	if otherHunter[1] > temp2 :
		if otherHunter[0] > temp2 :
			temp0 = -1 * temp3
		else:
			temp0 = min( prey[0] , otherHunter[0] )
	else:
		temp0 = min( otherHunter[1] , dist )
	temp0 = prey[1] - prey[0]
	temp1 = temp1 + otherHunter[1]
	temp1 = otherHunter[0] + temp3
	temp4 = max( dist , prey[0] )
	temp2 = dist * temp1
	if temp2 > otherHunter[1] :
		temp4 = min( dist , prey[0] )
	else:
		temp4 = min( prey[0] , temp3 )
	return [ dist , temp4 ]
