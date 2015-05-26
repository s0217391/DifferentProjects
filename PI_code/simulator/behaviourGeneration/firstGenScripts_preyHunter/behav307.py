#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	temp1 = min(temp0, temp0)
	temp0 = -1 * temp1
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	temp0 = temp1 * temp0
	temp0 = temp1 * prey[0]
	temp1 = max(temp1, prey[0])
	temp2 = max(temp0, prey[0])
	if prey[0] != 0:
		temp1 = temp1 / prey[0]
	else:
		temp1 = prey[0]
	temp0 = -1 * temp1
	temp0 = max(prey[0], temp2)
	if temp0 != 0:
		temp0 = temp0 / temp0
	else:
		temp0 = temp0
	return [prey[1], temp1]
