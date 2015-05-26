#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = prey[1] + prey[0]
	temp2 = max(prey[1], temp1)
	if prey[0] > prey[1]:
		if temp0 != 0:
			temp0 = temp1 / temp0
		else:
			temp0 = temp0
	else:
		temp0 = min(prey[1], temp2)
	temp1 = -1 * prey[1]
	temp3 = temp0 * temp2
	temp4 = -1 * temp0
	temp3 = max(prey[1], prey[1])
	if temp3 != 0:
		temp5 = temp3 / temp3
	else:
		temp5 = temp3
	temp0 = temp5 - temp5
	temp0 = temp5 + prey[1]
	return [temp5, temp4]
