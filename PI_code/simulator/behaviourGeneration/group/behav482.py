#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , otherHunter[0] )
	temp1 = prey[0] - prey[1]
	temp0 = temp1 * prey[1]
	temp0 = max( prey[1] , prey[1] )
	temp2 = prey[1] + prey[1]
	temp1 = max( otherHunter[0] , otherHunter[0] )
	if prey[1] != 0:
		temp3 = otherHunter[1] % prey[1]
	else:
		temp3 = prey[1]
	temp1 = max( otherHunter[0] , temp0 )
	if temp1 > temp3 :
		temp3 = min( otherHunter[1] , otherHunter[0] )
	else:
		temp3 = max( temp0 , prey[1] )
	temp3 = temp3 - otherHunter[1]
	if prey[1] != 0:
		temp3 = prey[1] % prey[1]
	else:
		temp3 = prey[1]
	temp4 = max( temp1 , otherHunter[0] )
	temp3 = min( prey[1] , temp3 )
	if otherHunter[0] != 0:
		temp3 = prey[0] / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp4 = prey[0] - temp0
	temp2 = dist * temp2
	temp2 = prey[0] + prey[0]
	if otherHunter[0] != 0:
		temp4 = prey[1] / otherHunter[0]
	else:
		temp4 = otherHunter[0]
	return [ prey[0] , otherHunter[0] ]
