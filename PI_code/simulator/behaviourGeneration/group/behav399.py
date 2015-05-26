#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , otherHunter[1] )
	temp1 = otherHunter[0] + temp0
	temp0 = min( prey[0] , dist )
	if otherHunter[0] > otherHunter[0] :
		if dist != 0:
			temp2 = otherHunter[1] % dist
		else:
			temp2 = dist
	else:
		temp2 = -1 * prey[0]
	temp3 = temp0 * dist
	if prey[1] != 0:
		temp2 = dist % prey[1]
	else:
		temp2 = prey[1]
	temp0 = -1 * temp1
	temp3 = min( temp1 , temp1 )
	if prey[1] != 0:
		temp0 = temp0 / prey[1]
	else:
		temp0 = prey[1]
	if temp0 > prey[0] :
		temp2 = temp2 + prey[1]
	else:
		temp2 = -1 * temp1
	temp2 = prey[0] * dist
	if prey[1] > prey[0] :
		temp2 = -1 * prey[0]
	else:
		if dist != 0:
			temp2 = temp2 / dist
		else:
			temp2 = dist
	if temp2 != 0:
		temp1 = otherHunter[1] % temp2
	else:
		temp1 = temp2
	temp0 = prey[0] - temp2
	temp1 = dist + otherHunter[1]
	if temp3 > temp1 :
		if prey[1] != 0:
			temp4 = prey[0] % prey[1]
		else:
			temp4 = prey[1]
	else:
		temp4 = -1 * temp0
	if prey[0] != 0:
		temp1 = temp2 / prey[0]
	else:
		temp1 = prey[0]
	if prey[1] > dist :
		if prey[1] != 0:
			temp3 = temp1 % prey[1]
		else:
			temp3 = prey[1]
	else:
		if temp1 != 0:
			temp3 = temp2 / temp1
		else:
			temp3 = temp1
	if dist > otherHunter[1] :
		temp5 = temp3 * otherHunter[1]
	else:
		temp5 = otherHunter[0] * temp0
	if otherHunter[0] > prey[0] :
		temp5 = temp1 * temp5
	else:
		temp5 = min( dist , temp1 )
	temp1 = max( prey[0] , temp2 )
	temp3 = prey[0] * temp2
	if otherHunter[1] > temp0 :
		temp2 = max( temp3 , temp2 )
	else:
		temp2 = -1 * prey[1]
	temp3 = prey[1] - temp1
	return [ temp1 , temp0 ]
