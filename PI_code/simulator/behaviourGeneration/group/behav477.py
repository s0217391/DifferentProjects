#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = dist / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if prey[1] != 0:
		temp1 = dist % prey[1]
	else:
		temp1 = prey[1]
	temp2 = prey[1] - prey[1]
	if otherHunter[1] != 0:
		temp1 = temp0 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[0] != 0:
		temp2 = temp1 / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp0 = temp1 + temp2
	temp2 = temp2 - otherHunter[0]
	temp1 = min( temp0 , prey[0] )
	if temp0 > temp1 :
		temp1 = temp2 - dist
	else:
		temp1 = temp1 - otherHunter[1]
	temp3 = dist - prey[0]
	temp4 = temp2 + temp0
	if prey[1] != 0:
		temp0 = dist / prey[1]
	else:
		temp0 = prey[1]
	temp4 = temp2 - dist
	if temp2 > otherHunter[1] :
		temp3 = dist - temp1
	else:
		temp3 = prey[0] * prey[1]
	return [ temp3 , prey[1] ]