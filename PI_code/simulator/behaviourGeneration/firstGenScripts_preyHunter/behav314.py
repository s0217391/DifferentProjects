#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = prey[1] - prey[1]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp1 = prey[0] - prey[0]
	temp0 = max(temp0, prey[0])
	temp0 = max(temp1, temp1)
	if temp1 > prey[0]:
		if temp1 > temp0:
			temp2 = prey[0] + prey[1]
		else:
			temp2 = min(temp0, prey[0])
	else:
		temp2 = temp0 - temp1
	if temp1 != 0:
		temp2 = temp0 / temp1
	else:
		temp2 = temp1
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp2 = -1 * prey[1]
	temp2 = temp0 - prey[1]
	temp3 = prey[1] * prey[1]
	temp4 = -1 * temp3
	temp5 = min(temp0, temp0)
	temp5 = prey[0] - temp4
	return [temp1, temp1]
