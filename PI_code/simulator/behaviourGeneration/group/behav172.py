#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp1 = -1 * temp0
	temp0 = temp1 - temp1
	if prey[1] != 0:
		temp2 = prey[0] % prey[1]
	else:
		temp2 = prey[1]
	temp2 = -1 * dist
	if otherHunter[1] > dist :
		temp3 = -1 * dist
	else:
		temp3 = min( prey[1] , otherHunter[0] )
	temp0 = max( temp2 , dist )
	temp2 = max( temp1 , dist )
	if dist > otherHunter[0] :
		temp0 = max( dist , prey[0] )
	else:
		temp0 = max( prey[0] , temp2 )
	temp3 = max( temp1 , dist )
	temp3 = max( temp2 , otherHunter[1] )
	if prey[1] != 0:
		temp2 = temp1 / prey[1]
	else:
		temp2 = prey[1]
	temp1 = temp2 + dist
	temp0 = max( prey[0] , temp3 )
	temp0 = max( otherHunter[0] , dist )
	temp0 = min( otherHunter[1] , otherHunter[0] )
	if otherHunter[1] != 0:
		temp2 = temp3 % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp4 = temp0 + prey[1]
	temp0 = temp3 * otherHunter[0]
	temp4 = prey[0] + otherHunter[1]
	return [ otherHunter[1] , prey[1] ]
