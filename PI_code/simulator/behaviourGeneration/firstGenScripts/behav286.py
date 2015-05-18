#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = prey[1] + prey[0]
	if temp0 > temp1:
		temp0 = -1 * temp1
	else:
		temp0 = temp1 * prey[1]
	if prey[1] != 0:
		temp0 = temp0 % prey[1]
	else:
		temp0 = prey[1]
	temp1 = min(prey[0], temp0)
	temp0 = prey[0] * prey[0]
	temp0 = prey[1] * temp0
	temp1 = prey[0] - prey[0]
	temp0 = min(temp1, temp0)
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	temp0 = -1 * prey[1]
	temp1 = temp0 * prey[1]
	temp0 = prey[0] + prey[0]
	if temp0 != 0:
		temp1 = prey[1] % temp0
	else:
		temp1 = temp0
	temp1 = prey[1] - temp1
	temp1 = temp0 * temp1
	return [prey[0], prey[0]]
