#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * dist
	temp1 = max( otherHunter[1] , temp0 )
	if temp0 > dist :
		temp2 = temp0 + temp1
	else:
		if temp0 > prey[1] :
			if prey[0] != 0:
				temp2 = temp1 % prey[0]
			else:
				temp2 = prey[0]
		else:
			if otherHunter[1] != 0:
				temp2 = otherHunter[1] % otherHunter[1]
			else:
				temp2 = otherHunter[1]
	if prey[1] != 0:
		temp0 = dist % prey[1]
	else:
		temp0 = prey[1]
	if temp0 > prey[0] :
		temp3 = temp1 + prey[0]
	else:
		if prey[0] > temp1 :
			temp3 = temp0 + temp1
		else:
			temp3 = otherHunter[0] + prey[0]
	if prey[0] != 0:
		temp2 = temp3 % prey[0]
	else:
		temp2 = prey[0]
	if prey[0] != 0:
		temp4 = otherHunter[0] % prey[0]
	else:
		temp4 = prey[0]
	temp2 = max( prey[1] , temp3 )
	temp0 = max( temp0 , otherHunter[0] )
	temp3 = min( dist , temp4 )
	temp3 = min( temp0 , prey[1] )
	temp4 = max( temp3 , otherHunter[0] )
	if prey[1] != 0:
		temp2 = temp2 / prey[1]
	else:
		temp2 = prey[1]
	temp2 = dist + temp0
	temp4 = temp4 * temp4
	temp3 = max( temp3 , prey[1] )
	temp1 = temp2 + temp4
	if otherHunter[1] != 0:
		temp2 = otherHunter[1] % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp5 = temp0 * otherHunter[0]
	if temp1 > otherHunter[1] :
		if dist != 0:
			temp0 = otherHunter[1] / dist
		else:
			temp0 = dist
	else:
		temp0 = temp2 * dist
	temp6 = min( temp5 , otherHunter[0] )
	temp0 = min( prey[1] , temp1 )
	return [ otherHunter[1] , dist ]
