#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = prey[0] + prey[0]
	temp2 = -1 * prey[1]
	temp0 = prey[0] * temp0
	if prey[0] > temp0:
		temp0 = min(temp1, prey[1])
	else:
		temp0 = max(temp1, prey[0])
	temp1 = temp0 * temp1
	temp2 = max(temp1, temp2)
	temp1 = max(prey[1], temp0)
	temp2 = prey[0] * temp0
	temp3 = -1 * temp1
	temp1 = temp2 + prey[1]
	temp3 = -1 * temp0
	if temp0 > temp2:
		temp0 = temp2 - temp1
	else:
		temp0 = min(temp2, temp0)
	temp0 = prey[0] - temp2
	return [prey[1], temp2]
