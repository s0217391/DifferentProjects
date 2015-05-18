#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	temp1 = prey[1] * prey[1]
	temp0 = prey[0] - prey[1]
	if prey[1] > prey[0]:
		temp2 = temp1 - temp1
	else:
		temp2 = prey[0] * prey[1]
	if temp1 != 0:
		temp0 = prey[0] / temp1
	else:
		temp0 = temp1
	temp1 = temp2 * prey[1]
	temp1 = temp0 - temp1
	temp0 = min(prey[0], temp2)
	temp1 = min(temp0, prey[1])
	temp0 = prey[0] + temp1
	temp1 = max(prey[1], temp2)
	temp1 = min(temp0, prey[0])
	temp2 = temp0 * temp0
	temp0 = prey[1] * prey[1]
	temp3 = temp2 + temp2
	if temp2 != 0:
		temp1 = prey[0] / temp2
	else:
		temp1 = temp2
	temp0 = max(temp0, temp2)
	temp3 = temp3 - prey[0]
	if temp1 != 0:
		temp2 = temp3 / temp1
	else:
		temp2 = temp1
	temp0 = prey[0] + temp1
	temp0 = max(prey[0], temp1)
	return [temp0, temp3]
