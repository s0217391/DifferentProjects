#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = prey[0] + temp0
	temp0 = max(temp1, temp0)
	temp2 = -1 * prey[0]
	temp3 = -1 * prey[1]
	if temp2 != 0:
		temp2 = temp3 % temp2
	else:
		temp2 = temp2
	temp1 = temp3 * prey[0]
	temp2 = max(temp1, temp2)
	temp0 = prey[0] + temp1
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	return [temp0, temp2]
