#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * prey[0]
	temp0 = max(prey[1], temp1)
	temp2 = temp1 + prey[1]
	temp3 = -1 * temp1
	temp1 = temp1 * temp1
	temp1 = min(temp2, temp2)
	temp4 = temp2 * prey[1]
	if temp4 != 0:
		temp2 = temp3 % temp4
	else:
		temp2 = temp4
	temp5 = min(prey[0], prey[1])
	temp2 = temp1 + prey[0]
	temp1 = -1 * temp2
	if temp2 != 0:
		temp6 = prey[0] % temp2
	else:
		temp6 = temp2
	temp5 = min(temp4, temp1)
	temp2 = temp2 * temp3
	return [temp0, temp6]
