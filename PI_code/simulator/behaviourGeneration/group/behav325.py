#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = dist % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = otherHunter[0] + prey[1]
	temp1 = min( dist , temp0 )
	temp1 = dist - temp0
	temp0 = temp0 + dist
	if dist > prey[0] :
		temp2 = min( prey[1] , otherHunter[0] )
	else:
		temp2 = -1 * prey[1]
	if temp1 > temp0 :
		temp1 = prey[0] - temp1
	else:
		temp1 = otherHunter[0] + prey[1]
	temp2 = otherHunter[1] - prey[0]
	if prey[1] != 0:
		temp3 = dist / prey[1]
	else:
		temp3 = prey[1]
	if prey[0] != 0:
		temp3 = temp2 % prey[0]
	else:
		temp3 = prey[0]
	temp3 = -1 * temp2
	temp2 = -1 * prey[0]
	temp2 = max( otherHunter[1] , otherHunter[1] )
	temp2 = max( temp2 , temp3 )
	temp4 = temp0 * temp0
	temp2 = max( temp3 , temp4 )
	return [ otherHunter[1] , temp0 ]
