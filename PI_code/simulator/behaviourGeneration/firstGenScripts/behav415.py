#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	temp1 = temp0 + prey[1]
	temp2 = prey[1] - temp1
	if prey[1] != 0:
		temp0 = temp2 / prey[1]
	else:
		temp0 = prey[1]
	temp0 = -1 * temp1
	temp0 = min(temp1, temp2)
	temp3 = temp2 - temp1
	if temp0 != 0:
		temp2 = temp2 % temp0
	else:
		temp2 = temp0
	if prey[0] != 0:
		temp1 = temp1 % prey[0]
	else:
		temp1 = prey[0]
	temp0 = max(temp3, temp1)
	temp4 = temp1 + temp1
	temp3 = prey[0] * prey[1]
	return [temp1, temp2]
