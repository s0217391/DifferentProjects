#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , otherHunter[0] )
	temp1 = otherHunter[0] - otherHunter[0]
	temp1 = min( prey[1] , dist )
	if temp0 > prey[0] :
		temp0 = otherHunter[1] - temp0
	else:
		if otherHunter[1] != 0:
			temp0 = dist % otherHunter[1]
		else:
			temp0 = otherHunter[1]
	temp1 = -1 * temp0
	if otherHunter[0] != 0:
		temp0 = prey[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = otherHunter[0] - prey[1]
	if prey[0] != 0:
		temp2 = otherHunter[0] / prey[0]
	else:
		temp2 = prey[0]
	temp2 = prey[0] * temp0
	temp0 = prey[1] + prey[0]
	temp3 = min( temp0 , prey[0] )
	temp4 = max( prey[1] , prey[1] )
	if prey[1] != 0:
		temp3 = dist % prey[1]
	else:
		temp3 = prey[1]
	temp4 = temp3 * temp2
	if temp2 > temp1 :
		temp3 = otherHunter[1] * otherHunter[0]
	else:
		temp3 = max( temp3 , prey[0] )
	if otherHunter[1] > temp1 :
		if prey[0] > temp2 :
			if prey[0] != 0:
				temp5 = dist % prey[0]
			else:
				temp5 = prey[0]
		else:
			temp5 = prey[0] * temp3
	else:
		temp5 = -1 * otherHunter[0]
	temp5 = min( prey[0] , otherHunter[1] )
	return [ temp4 , temp0 ]
