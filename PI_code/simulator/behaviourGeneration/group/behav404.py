#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , otherHunter[1] )
	temp1 = max( temp0 , dist )
	temp2 = min( temp1 , temp1 )
	temp3 = dist - temp1
	if temp2 != 0:
		temp3 = temp3 % temp2
	else:
		temp3 = temp2
	temp3 = otherHunter[0] + temp2
	temp1 = min( temp0 , prey[1] )
	if temp3 > dist :
		if temp1 != 0:
			temp2 = temp1 % temp1
		else:
			temp2 = temp1
	else:
		temp2 = temp3 + prey[0]
	return [ temp1 , temp1 ]
