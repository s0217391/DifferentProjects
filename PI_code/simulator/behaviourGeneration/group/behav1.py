#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[0] % prey[1]
	else:
		temp0 = prey[1]
	if otherHunter[0] > temp0 :
		temp1 = max( dist , prey[1] )
	else:
		temp1 = -1 * dist
	temp2 = otherHunter[1] * temp1
	temp0 = min( temp2 , otherHunter[1] )
	temp3 = temp0 * dist
	if prey[0] > temp2 :
		temp1 = temp0 * temp2
	else:
		temp1 = prey[0] * temp2
	temp1 = max( prey[0] , temp1 )
	if temp3 > temp0 :
		temp2 = max( otherHunter[1] , otherHunter[0] )
	else:
		temp2 = dist - temp0
	if temp3 != 0:
		temp0 = temp3 % temp3
	else:
		temp0 = temp3
	temp4 = max( temp1 , temp2 )
	temp5 = -1 * temp4
	temp4 = max( temp5 , temp3 )
	if temp1 != 0:
		temp0 = otherHunter[0] / temp1
	else:
		temp0 = temp1
	temp5 = temp3 - temp3
	temp0 = temp5 - prey[0]
	if temp1 != 0:
		temp3 = temp1 % temp1
	else:
		temp3 = temp1
	temp2 = min( prey[0] , temp5 )
	temp1 = prey[0] - temp3
	temp2 = otherHunter[1] + otherHunter[0]
	temp1 = max( prey[1] , otherHunter[0] )
	if temp5 != 0:
		temp2 = temp2 % temp5
	else:
		temp2 = temp5
	temp6 = otherHunter[0] + temp4
	return [ temp0 , temp0 ]
