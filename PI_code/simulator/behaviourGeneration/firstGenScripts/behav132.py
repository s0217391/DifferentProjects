#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(prey[0], temp0)
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	temp0 = temp0 - temp0
	if temp1 != 0:
		temp2 = prey[1] % temp1
	else:
		temp2 = temp1
	temp0 = prey[1] - prey[0]
	temp3 = -1 * prey[1]
	temp0 = -1 * temp0
	temp4 = temp0 - prey[0]
	temp5 = max(temp3, temp3)
	return [prey[0], temp1]
