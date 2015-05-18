#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	temp1 = prey[1] + prey[0]
	temp2 = temp0 - temp0
	temp3 = -1 * temp0
	temp3 = temp1 - temp3
	if temp3 != 0:
		temp3 = prey[1] / temp3
	else:
		temp3 = temp3
	temp3 = max(prey[0], temp1)
	temp0 = min(temp1, temp2)
	return [temp0, temp0]
