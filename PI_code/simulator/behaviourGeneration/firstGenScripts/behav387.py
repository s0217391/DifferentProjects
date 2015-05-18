#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = -1 * temp0
	temp2 = prey[1] * prey[1]
	temp3 = prey[0] - temp2
	temp0 = temp0 - temp0
	temp1 = -1 * prey[1]
	temp4 = min(temp0, temp0)
	temp4 = max(temp3, prey[0])
	temp0 = max(temp0, temp0)
	temp1 = max(temp3, temp2)
	temp2 = temp4 * temp4
	temp0 = temp1 + temp4
	if temp3 != 0:
		temp2 = prey[1] / temp3
	else:
		temp2 = temp3
	temp1 = temp0 - temp0
	temp4 = max(temp2, prey[1])
	temp3 = prey[1] - prey[1]
	temp1 = temp0 + temp0
	return [prey[0], temp0]
