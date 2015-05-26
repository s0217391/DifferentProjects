#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	if dist > dist :
		temp1 = min( otherHunter[1] , dist )
	else:
		temp1 = min( temp0 , temp0 )
	if otherHunter[0] != 0:
		temp0 = temp0 / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = -1 * prey[0]
	if prey[0] > prey[0] :
		temp1 = min( otherHunter[1] , prey[1] )
	else:
		temp1 = max( otherHunter[0] , dist )
	temp2 = otherHunter[1] + dist
	if prey[1] > dist :
		temp2 = temp0 * dist
	else:
		temp2 = max( temp1 , prey[0] )
	temp3 = min( prey[0] , temp1 )
	return [ temp0 , otherHunter[1] ]
