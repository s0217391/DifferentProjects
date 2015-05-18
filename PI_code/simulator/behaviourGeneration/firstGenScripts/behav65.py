#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp1 = prey[0] - prey[1]
	temp2 = temp0 + prey[0]
	temp0 = prey[1] - temp1
	temp2 = max(prey[1], temp0)
	temp0 = prey[1] + prey[1]
	if temp2 > temp2:
		if temp1 > prey[1]:
			temp2 = -1 * temp2
		else:
			temp2 = prey[1] - temp2
	else:
		temp2 = prey[0] * prey[1]
	temp3 = temp2 + prey[1]
	temp4 = max(prey[1], prey[0])
	temp4 = max(temp3, temp4)
	temp4 = temp0 + temp2
	temp2 = temp2 - temp2
	return [prey[1], temp3]
