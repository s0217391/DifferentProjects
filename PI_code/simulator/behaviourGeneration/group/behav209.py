#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] > otherHunter[0] :
		if otherHunter[1] > otherHunter[1] :
			temp0 = min( dist , dist )
		else:
			temp0 = max( prey[1] , otherHunter[1] )
	else:
		temp0 = dist * otherHunter[0]
	temp1 = max( temp0 , otherHunter[1] )
	temp2 = dist - temp1
	if temp1 != 0:
		temp3 = temp0 / temp1
	else:
		temp3 = temp1
	if temp3 != 0:
		temp2 = dist / temp3
	else:
		temp2 = temp3
	temp3 = min( prey[0] , temp1 )
	if dist != 0:
		temp0 = prey[1] % dist
	else:
		temp0 = dist
	temp4 = max( dist , temp1 )
	temp4 = max( prey[0] , otherHunter[0] )
	return [ temp2 , dist ]
