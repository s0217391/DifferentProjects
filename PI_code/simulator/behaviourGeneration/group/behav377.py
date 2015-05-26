#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = otherHunter[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = otherHunter[1] - prey[1]
	temp2 = prey[1] + prey[0]
	if prey[0] > temp1 :
		temp3 = max( temp1 , prey[1] )
	else:
		if otherHunter[1] != 0:
			temp3 = temp1 % otherHunter[1]
		else:
			temp3 = otherHunter[1]
	temp2 = max( temp0 , otherHunter[0] )
	if prey[1] > otherHunter[1] :
		if prey[0] > dist :
			if dist != 0:
				temp1 = temp2 / dist
			else:
				temp1 = dist
		else:
			temp1 = dist - temp0
	else:
		temp1 = max( otherHunter[0] , otherHunter[1] )
	temp4 = max( temp2 , temp0 )
	if temp4 != 0:
		temp3 = otherHunter[0] / temp4
	else:
		temp3 = temp4
	temp4 = min( temp1 , otherHunter[1] )
	temp4 = max( otherHunter[1] , otherHunter[1] )
	if dist > temp2 :
		temp5 = max( temp0 , temp1 )
	else:
		if dist != 0:
			temp5 = temp4 % dist
		else:
			temp5 = dist
	temp5 = temp4 - temp4
	temp6 = dist + temp4
	temp0 = temp4 - otherHunter[1]
	temp0 = -1 * temp3
	if temp6 > otherHunter[1] :
		temp3 = dist - temp6
	else:
		if temp0 > temp1 :
			temp3 = otherHunter[1] * temp6
		else:
			temp3 = temp5 - otherHunter[1]
	temp2 = prey[0] * temp5
	if temp5 != 0:
		temp5 = dist % temp5
	else:
		temp5 = temp5
	return [ otherHunter[1] , dist ]
