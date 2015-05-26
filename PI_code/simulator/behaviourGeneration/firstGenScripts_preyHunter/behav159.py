#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = min(prey[0], prey[1])
	temp0 = temp0 - prey[0]
	temp2 = max(temp0, temp0)
	temp0 = prey[0] * prey[0]
	temp3 = temp1 - temp1
	temp2 = prey[1] * temp3
	if temp2 > temp2:
		temp3 = min(temp0, temp1)
	else:
		temp3 = prey[0] - temp0
	temp0 = temp3 * prey[0]
	temp3 = min(temp3, prey[0])
	temp0 = temp0 + temp3
	temp0 = temp0 - temp0
	temp2 = max(prey[1], prey[1])
	temp1 = -1 * temp0
	temp2 = prey[0] * temp0
	temp3 = temp2 - temp1
	temp3 = temp3 - prey[0]
	if temp2 != 0:
		temp1 = temp1 % temp2
	else:
		temp1 = temp2
	return [temp1, prey[0]]
