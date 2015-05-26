#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = otherHunter[1] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = prey[0] * dist
	temp1 = temp1 + temp1
	temp2 = otherHunter[1] * dist
	temp2 = max( dist , prey[0] )
	temp1 = prey[1] + prey[0]
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	temp1 = prey[0] - prey[0]
	temp3 = otherHunter[1] + temp2
	temp1 = temp2 * temp2
	if otherHunter[0] != 0:
		temp2 = otherHunter[0] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp4 = otherHunter[1] + temp1
	if prey[1] > temp2 :
		if otherHunter[1] != 0:
			temp1 = dist / otherHunter[1]
		else:
			temp1 = otherHunter[1]
	else:
		temp1 = -1 * prey[0]
	temp0 = dist * temp2
	temp0 = max( temp2 , temp4 )
	temp2 = temp0 - temp3
	temp2 = max( prey[1] , temp1 )
	if temp0 != 0:
		temp3 = otherHunter[0] % temp0
	else:
		temp3 = temp0
	temp4 = -1 * temp1
	if temp4 != 0:
		temp5 = otherHunter[1] % temp4
	else:
		temp5 = temp4
	if dist > dist :
		temp3 = otherHunter[0] + temp1
	else:
		temp3 = min( temp0 , temp0 )
	if temp1 != 0:
		temp4 = temp5 % temp1
	else:
		temp4 = temp1
	return [ dist , dist ]
