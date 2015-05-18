#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	temp1 = min(prey[1], prey[0])
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	temp0 = min(prey[0], temp1)
	temp2 = -1 * temp0
	temp1 = prey[1] * prey[1]
	temp2 = min(temp2, prey[1])
	temp0 = max(temp0, temp2)
	temp3 = -1 * temp0
	temp3 = temp1 - prey[0]
	temp4 = -1 * prey[1]
	return [prey[0], temp2]
