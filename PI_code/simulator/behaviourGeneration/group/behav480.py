#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] > otherHunter[1] :
		temp0 = max( otherHunter[0] , prey[0] )
	else:
		if otherHunter[1] > dist :
			if otherHunter[1] != 0:
				temp0 = dist / otherHunter[1]
			else:
				temp0 = otherHunter[1]
		else:
			temp0 = min( dist , prey[1] )
	temp1 = -1 * otherHunter[1]
	temp2 = temp0 + prey[0]
	temp0 = min( prey[1] , dist )
	temp2 = temp0 + dist
	temp0 = dist - prey[0]
	if temp1 != 0:
		temp2 = prey[0] % temp1
	else:
		temp2 = temp1
	temp3 = max( otherHunter[0] , temp0 )
	temp1 = max( temp2 , temp0 )
	if otherHunter[1] > otherHunter[0] :
		temp2 = otherHunter[1] * dist
	else:
		temp2 = min( temp0 , prey[1] )
	temp4 = prey[1] + temp2
	temp1 = temp4 * temp4
	if otherHunter[0] != 0:
		temp0 = dist / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = otherHunter[1] + temp0
	if temp3 != 0:
		temp1 = prey[0] / temp3
	else:
		temp1 = temp3
	if temp4 > otherHunter[1] :
		temp5 = max( prey[1] , prey[0] )
	else:
		temp5 = otherHunter[0] * otherHunter[0]
	temp1 = max( temp1 , otherHunter[0] )
	if temp2 > temp5 :
		temp2 = min( prey[1] , dist )
	else:
		if temp5 != 0:
			temp2 = temp4 % temp5
		else:
			temp2 = temp5
	if otherHunter[1] != 0:
		temp4 = temp4 / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	temp2 = min( otherHunter[0] , prey[1] )
	if temp5 > prey[1] :
		temp3 = prey[0] + temp1
	else:
		if temp3 != 0:
			temp3 = otherHunter[0] / temp3
		else:
			temp3 = temp3
	temp2 = min( temp1 , otherHunter[1] )
	if otherHunter[0] > temp4 :
		if prey[0] != 0:
			temp4 = dist % prey[0]
		else:
			temp4 = prey[0]
	else:
		if temp4 > temp0 :
			temp4 = min( temp4 , temp1 )
		else:
			temp4 = otherHunter[1] + temp3
	if prey[0] != 0:
		temp4 = temp0 / prey[0]
	else:
		temp4 = prey[0]
	return [ temp4 , temp2 ]
