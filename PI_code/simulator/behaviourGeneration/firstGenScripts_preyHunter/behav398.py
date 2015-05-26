#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = prey[1] * prey[0]
	if temp0 > prey[1]:
		if temp1 != 0:
			temp2 = prey[1] / temp1
		else:
			temp2 = temp1
	else:
		temp2 = max(temp0, temp0)
	temp0 = max(temp1, temp0)
	temp3 = min(prey[1], temp1)
	return [temp2, prey[1]]
