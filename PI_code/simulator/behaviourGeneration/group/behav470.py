#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * otherHunter[1]
	temp1 = prey[0] * otherHunter[1]
	temp0 = min( dist , otherHunter[0] )
	if prey[0] > prey[1] :
		temp2 = min( dist , otherHunter[1] )
	else:
		temp2 = prey[0] + otherHunter[1]
	temp2 = temp2 + prey[0]
	temp3 = temp0 + temp0
	temp0 = max( dist , dist )
	temp0 = prey[0] + prey[1]
	if prey[1] > dist :
		temp1 = max( temp3 , otherHunter[0] )
	else:
		temp1 = otherHunter[0] - temp3
	return [ temp2 , temp0 ]
