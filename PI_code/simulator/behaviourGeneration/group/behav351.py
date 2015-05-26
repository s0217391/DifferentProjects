#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] > dist :
		if otherHunter[0] != 0:
			temp0 = dist % otherHunter[0]
		else:
			temp0 = otherHunter[0]
	else:
		temp0 = max( otherHunter[1] , prey[1] )
	if otherHunter[0] > otherHunter[0] :
		if dist != 0:
			temp1 = prey[1] % dist
		else:
			temp1 = dist
	else:
		temp1 = otherHunter[0] - prey[1]
	if prey[1] > temp0 :
		temp2 = -1 * dist
	else:
		temp2 = -1 * otherHunter[0]
	temp0 = min( otherHunter[1] , temp0 )
	if prey[0] != 0:
		temp2 = otherHunter[0] / prey[0]
	else:
		temp2 = prey[0]
	temp0 = max( temp1 , otherHunter[1] )
	temp2 = -1 * prey[1]
	temp3 = min( temp1 , temp0 )
	temp2 = temp2 - temp3
	if temp2 > temp2 :
		temp4 = temp2 + prey[0]
	else:
		temp4 = otherHunter[0] * prey[1]
	temp0 = dist + prey[0]
	if otherHunter[0] != 0:
		temp2 = prey[0] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp3 = otherHunter[0] - temp0
	temp0 = -1 * temp2
	temp1 = min( dist , otherHunter[0] )
	temp1 = -1 * prey[1]
	temp4 = temp1 + otherHunter[1]
	temp5 = otherHunter[1] * temp1
	temp5 = temp5 + temp3
	if temp3 != 0:
		temp5 = otherHunter[0] % temp3
	else:
		temp5 = temp3
	temp0 = temp2 * otherHunter[0]
	temp5 = temp2 * otherHunter[0]
	if prey[0] > temp3 :
		temp5 = min( dist , temp2 )
	else:
		if otherHunter[0] > temp1 :
			if temp4 != 0:
				temp5 = temp0 / temp4
			else:
				temp5 = temp4
		else:
			temp5 = temp2 * temp1
	return [ temp3 , dist ]
