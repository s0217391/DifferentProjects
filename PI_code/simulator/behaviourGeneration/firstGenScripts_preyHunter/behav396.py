#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	temp1 = prey[1] - temp0
	temp2 = temp1 * prey[1]
	if temp2 != 0:
		temp1 = temp2 % temp2
	else:
		temp1 = temp2
	if temp2 != 0:
		temp1 = temp2 / temp2
	else:
		temp1 = temp2
	temp1 = -1 * temp2
	temp3 = -1 * prey[0]
	temp2 = max(prey[1], temp1)
	if temp2 != 0:
		temp1 = prey[1] % temp2
	else:
		temp1 = temp2
	temp0 = temp1 + temp3
	if prey[1] != 0:
		temp4 = temp1 / prey[1]
	else:
		temp4 = prey[1]
	return [prey[1], temp2]
