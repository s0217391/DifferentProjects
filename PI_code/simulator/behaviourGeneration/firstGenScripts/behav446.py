#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[1]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp1 = prey[0] * prey[1]
	temp2 = temp0 * temp0
	temp3 = temp2 * prey[1]
	temp0 = temp3 * prey[0]
	temp3 = max(temp0, prey[1])
	temp2 = temp3 + temp0
	temp2 = temp2 + temp1
	temp1 = min(prey[0], prey[1])
	if temp2 > temp2:
		temp0 = temp0 * prey[0]
	else:
		if temp0 > temp2:
			temp0 = temp1 * prey[1]
		else:
			temp0 = temp1 * prey[1]
	if prey[0] > temp0:
		temp4 = prey[1] - temp0
	else:
		temp4 = temp1 - temp3
	temp3 = max(temp4, temp3)
	temp3 = min(temp3, temp4)
	temp2 = min(prey[0], temp4)
	return [temp3, temp4]
