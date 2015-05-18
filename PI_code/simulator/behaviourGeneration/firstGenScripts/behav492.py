#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	temp1 = prey[0] - prey[0]
	temp2 = prey[0] + prey[1]
	if temp0 > prey[0]:
		temp0 = temp2 * temp2
	else:
		if temp1 != 0:
			temp0 = prey[1] % temp1
		else:
			temp0 = temp1
	temp2 = -1 * prey[1]
	temp3 = -1 * temp2
	temp4 = -1 * temp2
	temp4 = temp4 + temp1
	temp5 = prey[1] * temp3
	temp5 = max(temp1, temp0)
	temp2 = temp0 * temp5
	if temp4 > prey[0]:
		temp6 = min(prey[1], temp3)
	else:
		temp6 = max(temp4, temp5)
	temp4 = min(temp1, temp4)
	temp0 = min(temp3, temp1)
	return [prey[0], temp1]
