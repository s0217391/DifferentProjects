#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > prey[0] :
		temp0 = prey[1] * dist
	else:
		temp0 = min( dist , otherHunter[1] )
	temp1 = otherHunter[0] * dist
	if otherHunter[0] > dist :
		if dist > temp1 :
			temp0 = otherHunter[1] + temp1
		else:
			if dist > otherHunter[0] :
				if prey[0] > temp0 :
					temp0 = min( temp1 , otherHunter[1] )
				else:
					temp0 = temp1 + temp1
			else:
				if otherHunter[0] != 0:
					temp0 = otherHunter[0] / otherHunter[0]
				else:
					temp0 = otherHunter[0]
	else:
		temp0 = temp0 - temp0
	if otherHunter[1] != 0:
		temp1 = temp0 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = min( prey[0] , prey[1] )
	temp0 = otherHunter[0] + temp0
	temp1 = max( otherHunter[1] , temp0 )
	temp1 = -1 * temp0
	temp0 = temp1 + prey[1]
	if prey[0] > otherHunter[1] :
		temp2 = max( temp1 , dist )
	else:
		temp2 = otherHunter[0] - otherHunter[0]
	if temp0 > otherHunter[0] :
		temp3 = max( otherHunter[0] , dist )
	else:
		temp3 = otherHunter[1] + otherHunter[1]
	if otherHunter[1] != 0:
		temp2 = temp0 % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp2 = max( prey[1] , temp0 )
	if dist != 0:
		temp3 = dist % dist
	else:
		temp3 = dist
	temp1 = -1 * prey[1]
	temp3 = otherHunter[1] - otherHunter[0]
	temp1 = temp2 - otherHunter[0]
	temp2 = max( prey[1] , temp3 )
	temp0 = temp1 * temp3
	return [ temp0 , dist ]
