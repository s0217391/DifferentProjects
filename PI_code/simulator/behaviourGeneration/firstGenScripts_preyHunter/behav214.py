#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	temp1 = min(prey[0], prey[1])
	if temp0 > prey[1]:
		if prey[1] != 0:
			temp1 = prey[1] % prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = min(prey[1], prey[0])
	temp1 = -1 * temp0
	temp2 = -1 * temp0
	temp0 = temp2 - prey[0]
	return [temp1, temp2]
