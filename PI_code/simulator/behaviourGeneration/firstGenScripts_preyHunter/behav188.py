#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	temp1 = prey[0] * temp0
	temp1 = temp0 - prey[1]
	temp1 = max(temp1, temp0)
	if temp1 != 0:
		temp1 = temp0 / temp1
	else:
		temp1 = temp1
	temp2 = max(temp1, temp0)
	temp1 = temp0 + temp1
	temp0 = temp2 * temp2
	temp0 = -1 * temp0
	if prey[0] != 0:
		temp3 = temp1 % prey[0]
	else:
		temp3 = prey[0]
	if prey[1] > prey[0]:
		temp2 = prey[0] + prey[0]
	else:
		temp2 = temp0 + temp0
	return [prey[1], prey[1]]
