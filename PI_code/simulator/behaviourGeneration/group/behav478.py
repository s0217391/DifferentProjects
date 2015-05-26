#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	if otherHunter[1] != 0:
		temp1 = prey[1] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = prey[0] + prey[1]
	temp1 = -1 * otherHunter[1]
	temp1 = dist - temp0
	temp0 = min( otherHunter[1] , prey[0] )
	temp1 = max( temp0 , otherHunter[1] )
	temp1 = min( prey[1] , otherHunter[0] )
	temp1 = max( prey[0] , prey[0] )
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp0 = prey[0] * prey[1]
	temp0 = prey[0] - prey[1]
	temp2 = prey[1] - temp0
	temp1 = max( temp0 , prey[1] )
	if temp1 != 0:
		temp0 = otherHunter[1] / temp1
	else:
		temp0 = temp1
	if temp2 > temp0 :
		temp3 = max( temp1 , prey[0] )
	else:
		if temp1 > otherHunter[0] :
			temp3 = min( otherHunter[1] , temp0 )
		else:
			if temp1 > otherHunter[1] :
				temp3 = temp0 - otherHunter[0]
			else:
				if temp0 > otherHunter[0] :
					if dist > otherHunter[1] :
						temp3 = temp1 * temp1
					else:
						temp3 = min( otherHunter[0] , dist )
				else:
					temp3 = prey[1] + temp2
	return [ temp3 , otherHunter[0] ]
