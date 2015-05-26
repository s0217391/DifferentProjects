#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + otherHunter[0]
	temp1 = -1 * temp0
	temp0 = max( otherHunter[0] , prey[1] )
	temp2 = temp0 + prey[0]
	if prey[0] != 0:
		temp2 = prey[0] / prey[0]
	else:
		temp2 = prey[0]
	if prey[1] != 0:
		temp3 = prey[0] % prey[1]
	else:
		temp3 = prey[1]
	temp4 = prey[1] + temp3
	if temp3 > temp2 :
		temp5 = -1 * otherHunter[0]
	else:
		temp5 = prey[1] * otherHunter[1]
	if otherHunter[1] != 0:
		temp1 = temp4 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if temp2 != 0:
		temp6 = otherHunter[1] % temp2
	else:
		temp6 = temp2
	if prey[1] != 0:
		temp6 = temp6 % prey[1]
	else:
		temp6 = prey[1]
	temp2 = min( temp1 , temp2 )
	temp3 = max( prey[1] , prey[0] )
	temp1 = min( temp5 , temp0 )
	if dist != 0:
		temp4 = prey[0] / dist
	else:
		temp4 = dist
	if temp0 > temp5 :
		temp7 = temp4 + temp3
	else:
		temp7 = temp3 - dist
	temp5 = temp3 - temp6
	if prey[1] > temp5 :
		temp3 = dist + prey[1]
	else:
		if temp7 != 0:
			temp3 = temp1 / temp7
		else:
			temp3 = temp7
	temp8 = -1 * dist
	temp1 = dist + temp1
	if temp3 != 0:
		temp0 = temp7 % temp3
	else:
		temp0 = temp3
	temp2 = temp6 - prey[1]
	temp5 = min( temp4 , otherHunter[1] )
	if prey[1] != 0:
		temp0 = temp0 / prey[1]
	else:
		temp0 = prey[1]
	temp5 = temp7 - temp3
	return [ otherHunter[1] , temp4 ]
