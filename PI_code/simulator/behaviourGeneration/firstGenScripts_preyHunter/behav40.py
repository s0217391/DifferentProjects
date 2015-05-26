#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = prey[0] * prey[0]
	temp2 = temp1 + prey[1]
	temp3 = max(temp1, prey[1])
	temp1 = temp1 + prey[0]
	if temp2 != 0:
		temp3 = temp3 / temp2
	else:
		temp3 = temp2
	temp1 = min(temp0, temp3)
	return [prey[1], temp2]
