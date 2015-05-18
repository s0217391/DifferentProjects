#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = prey[0] + temp0
	temp1 = min(temp0, prey[0])
	temp0 = min(temp1, temp0)
	if temp1 != 0:
		temp1 = temp1 % temp1
	else:
		temp1 = temp1
	temp2 = temp0 - prey[0]
	if prey[0] > prey[0]:
		if prey[1] != 0:
			temp0 = temp0 % prey[1]
		else:
			temp0 = prey[1]
	else:
		if temp2 != 0:
			temp0 = temp1 / temp2
		else:
			temp0 = temp2
	return [prey[1], prey[0]]
