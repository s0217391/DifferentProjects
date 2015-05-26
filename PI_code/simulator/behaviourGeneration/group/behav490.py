#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - dist
	temp1 = min( prey[0] , temp0 )
	if prey[1] != 0:
		temp2 = temp0 % prey[1]
	else:
		temp2 = prey[1]
	if temp2 > prey[1] :
		if otherHunter[1] != 0:
			temp3 = temp2 % otherHunter[1]
		else:
			temp3 = otherHunter[1]
	else:
		temp3 = prey[0] + otherHunter[0]
	temp1 = temp3 + temp3
	temp3 = otherHunter[0] + temp1
	temp0 = otherHunter[0] + prey[1]
	temp4 = min( otherHunter[1] , prey[1] )
	if temp0 != 0:
		temp4 = prey[0] / temp0
	else:
		temp4 = temp0
	temp5 = otherHunter[1] - temp0
	temp2 = temp3 - otherHunter[1]
	if temp1 > temp5 :
		temp2 = -1 * otherHunter[1]
	else:
		temp2 = -1 * dist
	temp5 = -1 * temp0
	temp3 = min( temp2 , otherHunter[1] )
	temp3 = prey[0] + temp3
	if prey[1] > temp2 :
		if temp2 != 0:
			temp6 = temp1 / temp2
		else:
			temp6 = temp2
	else:
		temp6 = prey[0] - temp5
	temp1 = otherHunter[0] + otherHunter[1]
	if otherHunter[1] > otherHunter[0] :
		temp5 = temp5 + prey[0]
	else:
		temp5 = temp3 + temp6
	temp7 = -1 * dist
	if temp6 > temp4 :
		if temp5 != 0:
			temp7 = prey[1] / temp5
		else:
			temp7 = temp5
	else:
		temp7 = -1 * otherHunter[1]
	temp1 = temp0 + temp5
	temp8 = min( temp1 , dist )
	temp2 = max( temp2 , temp2 )
	temp4 = min( otherHunter[1] , temp1 )
	return [ temp4 , temp8 ]
