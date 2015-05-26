#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > prey[0] :
		if dist != 0:
			temp0 = dist % dist
		else:
			temp0 = dist
	else:
		temp0 = max( prey[1] , dist )
	temp1 = prey[1] - prey[1]
	if otherHunter[1] != 0:
		temp1 = prey[0] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = -1 * temp1
	temp2 = -1 * dist
	temp3 = otherHunter[1] + temp2
	temp2 = temp0 + otherHunter[1]
	if prey[0] > prey[1] :
		if prey[0] > temp2 :
			temp4 = temp2 * temp1
		else:
			temp4 = min( otherHunter[0] , temp2 )
	else:
		temp4 = max( temp0 , temp0 )
	temp5 = -1 * prey[0]
	if otherHunter[1] != 0:
		temp4 = prey[0] % otherHunter[1]
	else:
		temp4 = otherHunter[1]
	temp6 = temp5 + otherHunter[1]
	temp2 = prey[1] * temp6
	temp0 = prey[0] - temp3
	temp5 = otherHunter[1] + prey[1]
	temp4 = -1 * temp3
	if prey[1] != 0:
		temp5 = temp2 / prey[1]
	else:
		temp5 = prey[1]
	temp0 = min( temp3 , temp2 )
	temp7 = min( temp0 , otherHunter[1] )
	if temp5 != 0:
		temp8 = temp2 % temp5
	else:
		temp8 = temp5
	if temp2 != 0:
		temp6 = temp8 / temp2
	else:
		temp6 = temp2
	if prey[1] != 0:
		temp6 = otherHunter[1] / prey[1]
	else:
		temp6 = prey[1]
	return [ temp6 , temp8 ]
