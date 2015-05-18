#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	temp1 = max(prey[0], prey[0])
	temp0 = temp0 * temp0
	temp1 = min(prey[1], prey[1])
	temp0 = -1 * temp0
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	temp0 = temp0 - temp1
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	temp1 = max(prey[1], temp0)
	temp0 = max(prey[0], prey[0])
	temp2 = min(prey[1], temp0)
	temp0 = temp2 - temp1
	return [temp2, temp2]
