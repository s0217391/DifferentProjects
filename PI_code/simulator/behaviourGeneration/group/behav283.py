#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	if prey[0] != 0:
		temp1 = prey[1] % prey[0]
	else:
		temp1 = prey[0]
	if otherHunter[1] > dist :
		temp1 = temp0 - prey[1]
	else:
		temp1 = min( prey[1] , temp1 )
	if temp0 > prey[1] :
		if dist != 0:
			temp2 = prey[1] % dist
		else:
			temp2 = dist
	else:
		if prey[1] != 0:
			temp2 = temp0 % prey[1]
		else:
			temp2 = prey[1]
	temp3 = max( temp1 , temp1 )
	if temp2 != 0:
		temp2 = prey[1] % temp2
	else:
		temp2 = temp2
	temp3 = min( otherHunter[0] , temp2 )
	temp2 = min( prey[0] , prey[0] )
	temp2 = temp1 * prey[0]
	temp2 = temp2 + otherHunter[0]
	temp2 = otherHunter[1] + prey[1]
	temp4 = temp1 - temp2
	temp3 = temp4 * temp3
	if prey[0] != 0:
		temp0 = temp1 / prey[0]
	else:
		temp0 = prey[0]
	temp3 = temp3 + prey[1]
	temp1 = dist * dist
	temp4 = temp2 + temp0
	temp0 = min( temp2 , dist )
	return [ prey[1] , otherHunter[1] ]
