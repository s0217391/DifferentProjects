#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , prey[0] )
	temp1 = temp0 + prey[1]
	if dist > dist :
		if temp0 > prey[0] :
			if otherHunter[0] != 0:
				temp1 = temp1 % otherHunter[0]
			else:
				temp1 = otherHunter[0]
		else:
			temp1 = max( temp1 , temp1 )
	else:
		temp1 = min( otherHunter[1] , temp1 )
	temp0 = dist - temp1
	temp0 = max( otherHunter[0] , dist )
	if temp0 != 0:
		temp2 = dist % temp0
	else:
		temp2 = temp0
	if temp2 > temp0 :
		temp0 = prey[0] - dist
	else:
		if prey[0] > otherHunter[1] :
			temp0 = prey[0] - temp1
		else:
			if temp0 != 0:
				temp0 = temp2 / temp0
			else:
				temp0 = temp0
	temp3 = max( otherHunter[0] , dist )
	return [ prey[1] , temp0 ]
