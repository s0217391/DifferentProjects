#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	temp1 = min(prey[1], temp1)
	temp1 = temp1 - prey[1]
	if temp0 != 0:
		temp2 = prey[0] % temp0
	else:
		temp2 = temp0
	temp3 = temp2 + temp2
	temp4 = temp3 - temp3
	temp0 = temp1 - temp1
	temp4 = max(prey[0], temp0)
	temp2 = -1 * temp4
	temp1 = temp1 * prey[0]
	return [temp0, temp0]
