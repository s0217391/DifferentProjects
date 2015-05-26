#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * dist
	if prey[0] != 0:
		temp1 = otherHunter[1] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = otherHunter[1] + prey[1]
	temp3 = dist - prey[0]
	temp1 = otherHunter[1] - prey[1]
	temp3 = temp1 + temp3
	temp4 = dist + prey[0]
	temp0 = max( temp0 , temp4 )
	if temp2 > temp0 :
		temp0 = otherHunter[1] - temp2
	else:
		temp0 = -1 * dist
	temp0 = min( prey[1] , temp4 )
	temp4 = otherHunter[0] + temp1
	if temp4 > temp0 :
		temp0 = prey[0] + temp2
	else:
		temp0 = otherHunter[1] + temp4
	if otherHunter[0] > prey[0] :
		temp2 = temp0 - temp4
	else:
		temp2 = min( temp2 , dist )
	if temp1 > otherHunter[0] :
		temp1 = max( temp0 , prey[0] )
	else:
		temp1 = temp1 - temp3
	temp4 = dist - otherHunter[1]
	if temp3 != 0:
		temp4 = otherHunter[0] % temp3
	else:
		temp4 = temp3
	if otherHunter[1] > temp2 :
		temp5 = -1 * temp4
	else:
		temp5 = max( temp2 , temp0 )
	if temp3 > temp2 :
		temp2 = otherHunter[1] * temp2
	else:
		if temp5 > temp1 :
			if prey[0] != 0:
				temp2 = temp1 % prey[0]
			else:
				temp2 = prey[0]
		else:
			if otherHunter[0] != 0:
				temp2 = temp5 / otherHunter[0]
			else:
				temp2 = otherHunter[0]
	temp0 = max( temp5 , temp2 )
	temp0 = max( temp4 , temp3 )
	temp1 = min( temp4 , prey[0] )
	return [ temp3 , temp3 ]
