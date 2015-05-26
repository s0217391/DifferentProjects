#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	if temp1 != 0:
		temp2 = prey[1] / temp1
	else:
		temp2 = temp1
	temp2 = prey[0] + temp0
	temp0 = max(prey[0], temp2)
	temp1 = temp0 * prey[1]
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[1] + temp2
	temp2 = temp2 - prey[0]
	temp0 = min(temp0, temp2)
	temp3 = temp2 + prey[1]
	temp1 = max(temp3, temp1)
	temp1 = prey[1] + temp0
	temp3 = min(prey[1], prey[0])
	temp2 = temp1 * temp0
	temp1 = min(temp1, temp0)
	temp2 = temp1 - prey[0]
	return [prey[0], prey[1]]
