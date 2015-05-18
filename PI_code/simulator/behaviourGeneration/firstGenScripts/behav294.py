#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	if temp0 != 0:
		temp1 = temp1 / temp0
	else:
		temp1 = temp0
	temp0 = min(prey[1], temp0)
	temp2 = temp1 - temp0
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	temp0 = max(temp2, prey[1])
	if prey[0] != 0:
		temp3 = temp1 / prey[0]
	else:
		temp3 = prey[0]
	if temp0 != 0:
		temp1 = temp1 % temp0
	else:
		temp1 = temp0
	if temp3 != 0:
		temp1 = temp0 / temp3
	else:
		temp1 = temp3
	temp1 = temp0 * prey[1]
	temp0 = max(temp1, temp1)
	temp4 = prey[0] * prey[1]
	return [prey[0], temp3]
