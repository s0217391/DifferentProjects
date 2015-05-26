#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[0] )
	temp1 = -1 * prey[1]
	temp0 = min( prey[1] , prey[1] )
	temp2 = max( dist , otherHunter[0] )
	temp3 = min( otherHunter[0] , dist )
	temp1 = dist * otherHunter[0]
	if temp3 != 0:
		temp1 = temp3 % temp3
	else:
		temp1 = temp3
	if otherHunter[1] != 0:
		temp4 = temp2 % otherHunter[1]
	else:
		temp4 = otherHunter[1]
	if temp4 != 0:
		temp4 = otherHunter[1] % temp4
	else:
		temp4 = temp4
	temp1 = temp1 - temp0
	temp5 = otherHunter[1] * temp0
	temp1 = temp4 - temp1
	if temp5 > temp3 :
		temp5 = temp2 * prey[0]
	else:
		if temp5 > dist :
			temp5 = min( temp0 , prey[1] )
		else:
			if prey[1] != 0:
				temp5 = temp3 % prey[1]
			else:
				temp5 = prey[1]
	if prey[0] != 0:
		temp4 = otherHunter[1] % prey[0]
	else:
		temp4 = prey[0]
	if temp2 != 0:
		temp4 = temp4 % temp2
	else:
		temp4 = temp2
	temp6 = -1 * temp4
	temp6 = dist * temp6
	if temp4 > prey[1] :
		if dist > temp0 :
			temp3 = temp2 + temp5
		else:
			if temp3 != 0:
				temp3 = prey[0] / temp3
			else:
				temp3 = temp3
	else:
		temp3 = temp6 * prey[0]
	if temp6 != 0:
		temp1 = temp6 / temp6
	else:
		temp1 = temp6
	if prey[1] != 0:
		temp7 = otherHunter[0] % prey[1]
	else:
		temp7 = prey[1]
	temp2 = temp7 * otherHunter[0]
	return [ prey[1] , otherHunter[0] ]
