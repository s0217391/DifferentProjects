#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	temp1 = min(prey[0], temp0)
	temp2 = -1 * temp1
	if temp2 != 0:
		temp0 = temp1 / temp2
	else:
		temp0 = temp2
	temp1 = -1 * prey[0]
	if temp0 != 0:
		temp1 = temp2 / temp0
	else:
		temp1 = temp0
	temp0 = min(prey[0], prey[1])
	temp2 = max(temp1, temp2)
	temp2 = max(temp2, prey[0])
	temp0 = prey[1] + prey[0]
	return [prey[1], temp1]
