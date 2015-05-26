#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , prey[1] )
	if dist > otherHunter[0] :
		if prey[1] != 0:
			temp1 = prey[0] % prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = otherHunter[1] - prey[1]
	temp2 = prey[1] - prey[0]
	temp2 = -1 * otherHunter[0]
	temp0 = max( otherHunter[1] , temp2 )
	temp2 = min( prey[0] , temp0 )
	temp2 = dist * otherHunter[0]
	temp3 = -1 * prey[1]
	temp4 = min( prey[1] , temp2 )
	temp3 = temp3 + dist
	if dist != 0:
		temp0 = otherHunter[1] / dist
	else:
		temp0 = dist
	if temp2 > temp1 :
		if temp2 != 0:
			temp5 = prey[1] % temp2
		else:
			temp5 = temp2
	else:
		temp5 = prey[0] + otherHunter[1]
	temp0 = prey[0] + temp1
	temp1 = min( temp0 , temp4 )
	temp0 = max( otherHunter[0] , temp4 )
	temp5 = temp1 - prey[0]
	temp0 = otherHunter[1] - temp3
	if temp2 != 0:
		temp6 = temp4 % temp2
	else:
		temp6 = temp2
	if temp1 != 0:
		temp0 = otherHunter[0] / temp1
	else:
		temp0 = temp1
	temp7 = min( temp2 , temp2 )
	temp3 = temp6 + temp4
	temp5 = temp0 * temp1
	if dist != 0:
		temp7 = temp7 % dist
	else:
		temp7 = dist
	temp8 = min( dist , otherHunter[0] )
	return [ temp2 , temp5 ]
