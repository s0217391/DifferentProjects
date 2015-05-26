#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = prey[0] * temp0
	temp0 = -1 * prey[1]
	temp0 = -1 * prey[1]
	temp1 = temp0 * prey[0]
	temp2 = min(prey[1], prey[0])
	temp0 = -1 * prey[0]
	temp2 = -1 * temp2
	temp2 = prey[1] - temp0
	temp2 = min(prey[1], temp2)
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	if temp0 != 0:
		temp3 = temp0 % temp0
	else:
		temp3 = temp0
	temp0 = prey[0] * prey[0]
	if prey[0] != 0:
		temp0 = temp1 / prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[0] - temp2
	temp2 = temp1 * temp3
	return [prey[0], prey[0]]
