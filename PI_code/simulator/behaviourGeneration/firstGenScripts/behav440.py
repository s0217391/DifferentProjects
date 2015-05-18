#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	temp1 = min(temp0, prey[1])
	temp2 = max(temp1, temp0)
	if prey[1] != 0:
		temp2 = prey[0] % prey[1]
	else:
		temp2 = prey[1]
	temp2 = temp1 * temp1
	if temp0 != 0:
		temp2 = prey[0] / temp0
	else:
		temp2 = temp0
	if temp2 != 0:
		temp3 = temp1 % temp2
	else:
		temp3 = temp2
	temp3 = min(temp2, prey[0])
	temp0 = min(temp1, temp1)
	temp3 = temp0 - temp1
	temp2 = temp2 * temp1
	temp2 = prey[0] * temp1
	return [temp1, prey[1]]
