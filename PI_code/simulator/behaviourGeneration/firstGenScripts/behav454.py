#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = min(prey[1], temp0)
	if prey[1] != 0:
		temp2 = prey[0] % prey[1]
	else:
		temp2 = prey[1]
	if temp0 != 0:
		temp0 = temp2 % temp0
	else:
		temp0 = temp0
	temp1 = prey[0] + temp1
	if temp0 != 0:
		temp1 = temp2 / temp0
	else:
		temp1 = temp0
	temp3 = temp0 * temp0
	if temp3 != 0:
		temp1 = temp2 % temp3
	else:
		temp1 = temp3
	return [prey[1], prey[0]]
