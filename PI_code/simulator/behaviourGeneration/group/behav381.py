#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * otherHunter[0]
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp2 = temp1 * otherHunter[1]
	temp3 = -1 * dist
	temp4 = min( prey[1] , temp2 )
	temp0 = min( otherHunter[1] , temp0 )
	temp3 = temp0 - temp0
	if temp3 != 0:
		temp0 = temp3 / temp3
	else:
		temp0 = temp3
	temp5 = min( temp3 , temp1 )
	if temp2 > temp0 :
		if temp4 != 0:
			temp1 = temp0 / temp4
		else:
			temp1 = temp4
	else:
		temp1 = dist - prey[0]
	if prey[0] != 0:
		temp4 = otherHunter[1] / prey[0]
	else:
		temp4 = prey[0]
	if temp3 != 0:
		temp1 = temp0 / temp3
	else:
		temp1 = temp3
	temp3 = min( otherHunter[0] , temp1 )
	temp3 = -1 * temp1
	temp3 = otherHunter[1] + otherHunter[1]
	if prey[1] != 0:
		temp6 = temp3 / prey[1]
	else:
		temp6 = prey[1]
	temp7 = otherHunter[0] * temp2
	temp5 = max( temp5 , temp3 )
	if temp0 > otherHunter[1] :
		temp4 = -1 * temp0
	else:
		temp4 = prey[1] - temp5
	if temp3 != 0:
		temp4 = dist / temp3
	else:
		temp4 = temp3
	temp7 = temp4 + prey[1]
	temp2 = min( temp0 , temp1 )
	if temp7 > temp7 :
		temp2 = temp0 - temp4
	else:
		temp2 = prey[0] * otherHunter[1]
	temp3 = min( temp1 , otherHunter[0] )
	return [ temp1 , temp6 ]
