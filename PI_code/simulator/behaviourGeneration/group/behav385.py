#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , dist )
	temp1 = min( prey[0] , otherHunter[0] )
	temp0 = dist - temp0
	if temp1 != 0:
		temp2 = otherHunter[0] / temp1
	else:
		temp2 = temp1
	if prey[1] != 0:
		temp1 = prey[1] / prey[1]
	else:
		temp1 = prey[1]
	if temp2 > prey[1] :
		if otherHunter[0] != 0:
			temp3 = otherHunter[0] / otherHunter[0]
		else:
			temp3 = otherHunter[0]
	else:
		if otherHunter[1] > otherHunter[0] :
			temp3 = otherHunter[1] - temp2
		else:
			temp3 = otherHunter[0] + temp1
	temp4 = min( otherHunter[0] , otherHunter[0] )
	temp4 = temp0 + temp0
	if temp2 > temp3 :
		temp3 = -1 * otherHunter[1]
	else:
		if prey[0] != 0:
			temp3 = otherHunter[0] / prey[0]
		else:
			temp3 = prey[0]
	temp1 = temp4 * temp0
	if otherHunter[0] != 0:
		temp3 = temp0 / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp3 = max( otherHunter[0] , dist )
	temp2 = prey[1] + temp1
	temp2 = -1 * temp0
	temp0 = min( temp4 , temp3 )
	if temp2 != 0:
		temp3 = prey[0] % temp2
	else:
		temp3 = temp2
	if temp1 > prey[1] :
		temp4 = -1 * prey[1]
	else:
		temp4 = temp1 + otherHunter[0]
	return [ temp1 , otherHunter[0] ]
