#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[1] * prey[0]
	temp2 = prey[1] * temp1
	temp0 = prey[1] * temp0
	temp2 = min(prey[1], temp2)
	if temp1 != 0:
		temp0 = prey[0] % temp1
	else:
		temp0 = temp1
	temp2 = max(temp1, prey[1])
	temp1 = -1 * temp0
	temp3 = temp1 * prey[1]
	temp4 = min(prey[0], prey[1])
	temp3 = prey[1] + temp0
	if temp1 != 0:
		temp3 = temp1 % temp1
	else:
		temp3 = temp1
	temp4 = -1 * prey[0]
	if temp2 != 0:
		temp0 = prey[0] / temp2
	else:
		temp0 = temp2
	temp4 = temp3 + temp3
	temp0 = temp3 + temp1
	temp5 = min(prey[1], temp4)
	temp1 = max(temp0, temp1)
	return [temp5, temp4]
