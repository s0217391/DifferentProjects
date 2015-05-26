#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > dist :
		if prey[1] != 0:
			temp0 = prey[0] / prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = max( prey[0] , otherHunter[1] )
	if dist != 0:
		temp1 = otherHunter[0] % dist
	else:
		temp1 = dist
	temp2 = prey[0] + temp0
	temp2 = max( temp2 , temp1 )
	temp0 = max( otherHunter[0] , otherHunter[0] )
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	temp0 = min( temp0 , dist )
	temp1 = otherHunter[1] - otherHunter[0]
	if temp1 > temp2 :
		temp0 = max( temp2 , temp0 )
	else:
		temp0 = max( temp0 , temp1 )
	temp0 = max( prey[1] , temp1 )
	temp1 = min( otherHunter[0] , temp0 )
	temp1 = temp0 * otherHunter[0]
	if otherHunter[1] != 0:
		temp1 = temp2 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if dist > otherHunter[0] :
		if otherHunter[1] > otherHunter[1] :
			if otherHunter[1] != 0:
				temp3 = temp0 % otherHunter[1]
			else:
				temp3 = otherHunter[1]
		else:
			temp3 = max( temp0 , temp2 )
	else:
		if otherHunter[1] > dist :
			temp3 = temp2 + dist
		else:
			temp3 = temp1 - temp1
	temp2 = otherHunter[1] - otherHunter[0]
	return [ dist , prey[1] ]
