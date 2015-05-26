#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = max(prey[0], temp0)
	if temp1 != 0:
		temp0 = prey[0] % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp0 = temp1 % prey[0]
	else:
		temp0 = prey[0]
	temp2 = prey[0] - prey[0]
	temp2 = max(temp0, temp0)
	temp1 = temp1 - temp2
	return [prey[0], temp1]
