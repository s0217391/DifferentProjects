#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	if temp0 > prey[1]:
		temp1 = -1 * temp0
	else:
		temp1 = prey[1] + temp0
	temp0 = temp1 + prey[0]
	if temp0 != 0:
		temp0 = prey[1] / temp0
	else:
		temp0 = temp0
	temp1 = max(temp0, prey[1])
	temp0 = min(temp0, prey[0])
	if prey[1] > prey[0]:
		temp1 = prey[0] * prey[1]
	else:
		if temp0 != 0:
			temp1 = temp1 / temp0
		else:
			temp1 = temp0
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	return [prey[0], temp0]
