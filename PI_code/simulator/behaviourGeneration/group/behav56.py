#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[1]
	if prey[1] > dist :
		temp1 = -1 * otherHunter[1]
	else:
		temp1 = min( dist , otherHunter[1] )
	if prey[1] != 0:
		temp1 = otherHunter[1] / prey[1]
	else:
		temp1 = prey[1]
	temp2 = prey[1] + otherHunter[1]
	temp3 = min( temp1 , temp2 )
	return [ otherHunter[1] , dist ]
