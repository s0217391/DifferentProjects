#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[1] :
		temp0 = min( otherHunter[1] , otherHunter[0] )
	else:
		temp0 = dist + prey[0]
	temp1 = max( prey[1] , temp0 )
	temp2 = max( temp1 , prey[0] )
	temp1 = min( prey[1] , dist )
	temp0 = max( temp2 , temp2 )
	temp1 = min( temp0 , temp0 )
	temp2 = max( temp1 , otherHunter[1] )
	temp0 = otherHunter[0] - otherHunter[0]
	temp3 = min( prey[0] , temp0 )
	if temp3 != 0:
		temp4 = otherHunter[1] % temp3
	else:
		temp4 = temp3
	if dist > dist :
		temp4 = max( temp0 , otherHunter[0] )
	else:
		temp4 = temp2 - temp3
	return [ otherHunter[0] , temp2 ]
