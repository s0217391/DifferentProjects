#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = max(prey[1], prey[0])
	temp1 = prey[1] * prey[0]
	temp1 = -1 * temp1
	temp0 = min(prey[0], prey[0])
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	if temp0 > prey[0]:
		temp1 = min(prey[1], temp1)
	else:
		temp1 = temp0 * prey[0]
	temp1 = -1 * temp0
	if prey[0] > temp1:
		temp0 = prey[0] + temp1
	else:
		temp0 = -1 * prey[1]
	temp0 = temp0 + temp1
	temp1 = temp0 * temp1
	if prey[1] > temp1:
		temp1 = min(temp0, temp0)
	else:
		temp1 = -1 * temp0
	temp1 = temp0 - temp1
	temp0 = temp1 - prey[0]
	return [prey[1], prey[0]]
