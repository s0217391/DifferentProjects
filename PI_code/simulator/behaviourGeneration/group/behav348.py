#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , dist )
	temp1 = dist * prey[0]
	temp2 = min( prey[0] , dist )
	if dist != 0:
		temp2 = temp0 / dist
	else:
		temp2 = dist
	temp2 = min( temp2 , prey[1] )
	temp0 = temp2 + temp2
	temp2 = temp1 - prey[0]
	temp1 = max( temp1 , temp0 )
	temp1 = temp2 + otherHunter[1]
	if otherHunter[0] > temp1 :
		temp1 = -1 * otherHunter[1]
	else:
		if temp0 > temp1 :
			temp1 = max( dist , dist )
		else:
			if prey[1] != 0:
				temp1 = otherHunter[1] % prey[1]
			else:
				temp1 = prey[1]
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	return [ otherHunter[0] , otherHunter[0] ]
