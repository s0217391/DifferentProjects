#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = prey[0] * prey[0]
	temp0 = -1 * prey[1]
	temp0 = min(temp1, prey[1])
	temp2 = max(prey[1], prey[1])
	if temp0 > prey[1]:
		if temp1 > prey[0]:
			temp3 = prey[1] * prey[0]
		else:
			if temp1 > prey[0]:
				temp3 = -1 * prey[1]
			else:
				temp3 = prey[0] + temp0
	else:
		temp3 = max(prey[0], temp0)
	return [temp3, prey[0]]
