#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[0] :
		temp0 = min( otherHunter[0] , dist )
	else:
		temp0 = prey[1] * prey[0]
	if otherHunter[1] > prey[1] :
		if otherHunter[1] != 0:
			temp1 = prey[1] / otherHunter[1]
		else:
			temp1 = otherHunter[1]
	else:
		temp1 = max( otherHunter[0] , prey[0] )
	if temp0 != 0:
		temp2 = otherHunter[0] / temp0
	else:
		temp2 = temp0
	if otherHunter[1] != 0:
		temp0 = temp0 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = min( otherHunter[0] , prey[0] )
	temp0 = otherHunter[0] * temp0
	temp3 = otherHunter[1] + temp2
	if otherHunter[1] != 0:
		temp0 = otherHunter[0] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp0 = otherHunter[0] - otherHunter[1]
	if otherHunter[0] != 0:
		temp3 = temp3 % otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp0 = min( dist , otherHunter[1] )
	temp3 = temp2 + prey[1]
	temp3 = otherHunter[1] - prey[0]
	temp2 = -1 * prey[0]
	if otherHunter[1] != 0:
		temp3 = dist % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp3 = temp2 * temp2
	temp3 = otherHunter[0] - temp3
	if temp0 > temp1 :
		temp3 = prey[0] - otherHunter[1]
	else:
		if temp3 != 0:
			temp3 = temp3 / temp3
		else:
			temp3 = temp3
	temp3 = -1 * prey[0]
	temp3 = -1 * temp2
	if temp2 != 0:
		temp4 = temp2 % temp2
	else:
		temp4 = temp2
	temp1 = dist + otherHunter[0]
	if temp1 != 0:
		temp0 = prey[0] / temp1
	else:
		temp0 = temp1
	return [ temp1 , otherHunter[1] ]
