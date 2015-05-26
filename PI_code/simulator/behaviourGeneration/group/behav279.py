#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , prey[1] )
	temp1 = max( otherHunter[0] , otherHunter[0] )
	temp1 = otherHunter[0] + temp0
	if dist > prey[1] :
		temp1 = prey[1] * otherHunter[1]
	else:
		temp1 = max( dist , otherHunter[0] )
	temp2 = min( prey[1] , otherHunter[1] )
	if otherHunter[0] != 0:
		temp3 = dist / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp1 = min( temp2 , otherHunter[0] )
	temp3 = min( prey[0] , temp2 )
	if temp0 != 0:
		temp0 = temp3 / temp0
	else:
		temp0 = temp0
	temp0 = prey[0] * temp3
	temp0 = min( temp3 , otherHunter[0] )
	temp1 = prey[0] * dist
	temp0 = min( dist , temp1 )
	if prey[0] > otherHunter[1] :
		temp3 = -1 * otherHunter[0]
	else:
		temp3 = temp1 - temp1
	temp1 = max( prey[0] , dist )
	temp0 = otherHunter[0] - temp0
	temp2 = temp2 - temp2
	temp3 = min( temp0 , prey[1] )
	if dist > temp2 :
		temp2 = temp1 - dist
	else:
		temp2 = temp2 - prey[0]
	if prey[1] != 0:
		temp0 = temp0 % prey[1]
	else:
		temp0 = prey[1]
	temp0 = temp0 - otherHunter[0]
	if otherHunter[1] > dist :
		if otherHunter[0] != 0:
			temp0 = temp1 % otherHunter[0]
		else:
			temp0 = otherHunter[0]
	else:
		if temp1 > prey[1] :
			if temp0 != 0:
				temp0 = dist / temp0
			else:
				temp0 = temp0
		else:
			temp0 = -1 * dist
	if otherHunter[1] != 0:
		temp0 = temp0 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	return [ temp1 , temp1 ]
