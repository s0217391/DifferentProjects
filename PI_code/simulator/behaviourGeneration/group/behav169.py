#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[1] , dist )
	temp1 = max( otherHunter[1] , dist )
	if otherHunter[0] > temp1 :
		temp0 = min( temp1 , prey[0] )
	else:
		temp0 = temp0 - prey[1]
	temp0 = min( prey[1] , otherHunter[0] )
	temp1 = max( temp1 , otherHunter[1] )
	temp1 = prey[0] + otherHunter[0]
	if temp0 > prey[0] :
		temp0 = otherHunter[1] - prey[1]
	else:
		temp0 = max( temp0 , prey[0] )
	temp2 = max( otherHunter[1] , prey[1] )
	temp0 = otherHunter[1] + temp0
	temp3 = temp1 + prey[0]
	if temp3 != 0:
		temp0 = dist / temp3
	else:
		temp0 = temp3
	temp2 = -1 * temp0
	temp0 = temp2 + temp3
	temp3 = temp3 * temp1
	temp1 = min( prey[1] , temp2 )
	temp2 = temp3 - dist
	temp3 = otherHunter[0] * prey[0]
	temp1 = dist + dist
	if temp1 > dist :
		temp2 = -1 * temp1
	else:
		temp2 = min( prey[0] , temp1 )
	temp2 = temp0 + otherHunter[0]
	return [ prey[0] , temp2 ]
