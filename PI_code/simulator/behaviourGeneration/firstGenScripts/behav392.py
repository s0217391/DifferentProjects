#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = temp0 - prey[0]
	temp2 = temp1 * prey[1]
	temp1 = min(temp1, temp2)
	if temp2 != 0:
		temp1 = temp0 / temp2
	else:
		temp1 = temp2
	if temp1 != 0:
		temp3 = temp2 % temp1
	else:
		temp3 = temp1
	temp4 = max(prey[1], temp0)
	temp1 = max(prey[1], temp0)
	temp1 = temp0 - temp2
	temp1 = -1 * prey[1]
	temp3 = temp1 + temp1
	temp5 = -1 * temp1
	temp2 = min(prey[0], temp4)
	temp1 = max(temp5, temp2)
	return [temp3, temp3]
