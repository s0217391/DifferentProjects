#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = max(prey[1], temp0)
	if prey[1] > temp1:
		temp0 = min(temp1, prey[0])
	else:
		temp0 = temp1 - prey[0]
	temp0 = min(prey[0], prey[1])
	temp1 = max(temp1, prey[1])
	temp1 = prey[0] + prey[1]
	if temp1 > prey[0]:
		temp0 = prey[1] - prey[0]
	else:
		temp0 = max(temp1, prey[0])
	temp2 = max(temp0, prey[0])
	temp0 = prey[1] + temp1
	temp3 = temp1 + prey[0]
	if temp3 != 0:
		temp0 = temp0 / temp3
	else:
		temp0 = temp3
	temp2 = -1 * temp1
	temp0 = temp3 + temp3
	temp3 = temp3 * temp2
	temp1 = min(prey[0], temp3)
	temp2 = temp3 - temp0
	temp3 = prey[1] * prey[0]
	temp1 = temp1 + temp1
	if temp2 > temp1:
		temp2 = -1 * temp2
	else:
		temp2 = min(prey[0], temp2)
	temp2 = temp1 + prey[1]
	return [prey[0], temp3]
