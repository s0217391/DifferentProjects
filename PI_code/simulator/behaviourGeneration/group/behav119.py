#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - prey[1]
	if otherHunter[1] > otherHunter[1] :
		temp1 = max( dist , prey[0] )
	else:
		temp1 = otherHunter[0] - temp0
	temp2 = dist + prey[0]
	if prey[0] != 0:
		temp3 = temp1 % prey[0]
	else:
		temp3 = prey[0]
	temp3 = temp3 + prey[0]
	temp4 = min( prey[1] , temp2 )
	temp1 = temp3 + temp0
	temp3 = prey[1] - temp3
	if temp0 > prey[1] :
		if temp2 != 0:
			temp4 = temp0 % temp2
		else:
			temp4 = temp2
	else:
		temp4 = prey[1] - temp3
	temp5 = temp1 - dist
	temp2 = min( otherHunter[0] , temp2 )
	temp0 = prey[0] + temp0
	if prey[0] != 0:
		temp0 = otherHunter[0] % prey[0]
	else:
		temp0 = prey[0]
	temp5 = min( temp0 , temp1 )
	temp6 = min( temp1 , temp4 )
	temp2 = temp5 + temp1
	if dist != 0:
		temp0 = temp5 % dist
	else:
		temp0 = dist
	if prey[1] > prey[0] :
		if temp0 != 0:
			temp5 = prey[0] % temp0
		else:
			temp5 = temp0
	else:
		temp5 = prey[1] + prey[1]
	if temp1 != 0:
		temp7 = temp4 / temp1
	else:
		temp7 = temp1
	return [ temp7 , otherHunter[1] ]
