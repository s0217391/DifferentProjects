#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	temp1 = max(prey[0], prey[0])
	temp2 = prey[1] + prey[0]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp3 = temp1 * temp0
	temp1 = prey[0] + temp1
	temp0 = temp2 * prey[0]
	if temp3 != 0:
		temp3 = temp1 / temp3
	else:
		temp3 = temp3
	if temp2 > prey[0]:
		temp2 = temp0 - temp0
	else:
		if temp2 != 0:
			temp2 = temp0 % temp2
		else:
			temp2 = temp2
	temp3 = max(temp3, prey[1])
	temp3 = min(prey[0], temp1)
	temp3 = prey[0] + temp2
	if temp0 > temp2:
		temp2 = temp2 * temp2
	else:
		temp2 = prey[0] * temp3
	temp4 = max(temp1, prey[1])
	return [temp1, temp4]
