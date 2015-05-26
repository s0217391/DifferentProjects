#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = prey[0] - temp0
	temp1 = max(temp0, prey[0])
	temp0 = -1 * temp1
	temp0 = max(temp0, prey[0])
	temp2 = temp0 * prey[0]
	temp3 = -1 * prey[0]
	temp2 = max(temp0, temp0)
	if temp1 > temp2:
		temp2 = -1 * temp1
	else:
		if temp3 != 0:
			temp2 = prey[0] / temp3
		else:
			temp2 = temp3
	temp3 = min(prey[0], temp1)
	return [prey[0], temp1]
