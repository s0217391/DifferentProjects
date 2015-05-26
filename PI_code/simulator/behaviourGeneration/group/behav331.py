#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[1] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = min( otherHunter[1] , prey[0] )
	if temp0 > dist :
		temp0 = temp0 + temp1
	else:
		temp0 = temp1 * temp1
	if dist != 0:
		temp2 = otherHunter[0] / dist
	else:
		temp2 = dist
	if otherHunter[1] != 0:
		temp3 = temp0 % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp3 = max( prey[1] , temp2 )
	temp4 = min( otherHunter[1] , prey[1] )
	if temp0 > prey[1] :
		temp5 = temp4 + temp1
	else:
		temp5 = temp0 * temp4
	temp5 = temp0 * dist
	temp5 = temp3 + temp1
	if otherHunter[1] != 0:
		temp2 = temp0 / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if otherHunter[0] != 0:
		temp6 = otherHunter[0] / otherHunter[0]
	else:
		temp6 = otherHunter[0]
	if temp1 != 0:
		temp5 = otherHunter[1] / temp1
	else:
		temp5 = temp1
	temp0 = temp6 * temp5
	temp7 = -1 * temp0
	temp5 = min( prey[1] , temp3 )
	temp1 = temp6 + temp0
	temp5 = min( temp7 , temp3 )
	temp1 = temp1 + temp4
	if dist != 0:
		temp7 = prey[0] % dist
	else:
		temp7 = dist
	temp8 = min( temp2 , otherHunter[1] )
	temp3 = min( temp1 , temp0 )
	temp8 = prey[1] + temp8
	if temp7 > otherHunter[0] :
		temp7 = -1 * temp6
	else:
		temp7 = min( otherHunter[1] , temp3 )
	return [ otherHunter[0] , prey[0] ]
