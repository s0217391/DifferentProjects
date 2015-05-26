#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + otherHunter[0]
	temp1 = -1 * temp0
	temp1 = otherHunter[0] - dist
	temp0 = temp0 + prey[1]
	if temp1 > dist :
		if otherHunter[1] != 0:
			temp1 = otherHunter[1] % otherHunter[1]
		else:
			temp1 = otherHunter[1]
	else:
		temp1 = max( prey[0] , dist )
	if prey[0] != 0:
		temp2 = dist / prey[0]
	else:
		temp2 = prey[0]
	temp2 = max( prey[0] , prey[1] )
	temp2 = temp0 * otherHunter[1]
	temp3 = otherHunter[1] - temp1
	if temp1 > temp1 :
		temp4 = -1 * temp1
	else:
		temp4 = temp3 + prey[1]
	temp2 = temp2 + temp0
	temp3 = max( prey[1] , prey[0] )
	if temp1 > otherHunter[1] :
		temp3 = temp2 - temp3
	else:
		temp3 = prey[1] * temp3
	temp3 = dist * otherHunter[0]
	temp0 = temp4 * otherHunter[1]
	if temp0 > temp0 :
		if otherHunter[0] > temp0 :
			temp1 = -1 * dist
		else:
			temp1 = -1 * temp2
	else:
		temp1 = -1 * prey[0]
	temp4 = otherHunter[0] * temp3
	temp0 = min( temp1 , prey[0] )
	if otherHunter[0] > temp1 :
		temp3 = max( temp4 , prey[1] )
	else:
		temp3 = otherHunter[0] + temp0
	if prey[1] > dist :
		temp4 = dist - otherHunter[1]
	else:
		temp4 = min( temp2 , dist )
	temp5 = max( temp4 , temp1 )
	temp0 = -1 * otherHunter[1]
	temp3 = max( temp0 , temp3 )
	temp4 = otherHunter[1] * temp0
	if temp5 != 0:
		temp5 = dist % temp5
	else:
		temp5 = temp5
	return [ dist , temp5 ]
