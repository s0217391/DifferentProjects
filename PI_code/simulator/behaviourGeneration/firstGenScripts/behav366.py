#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = prey[0] - prey[1]
	temp2 = prey[1] + temp0
	if temp1 != 0:
		temp2 = temp1 / temp1
	else:
		temp2 = temp1
	temp1 = prey[1] + prey[1]
	if prey[0] != 0:
		temp3 = prey[0] / prey[0]
	else:
		temp3 = prey[0]
	temp0 = min(temp3, temp0)
	temp4 = min(prey[1], prey[0])
	temp2 = min(prey[1], temp0)
	if temp0 != 0:
		temp1 = temp4 % temp0
	else:
		temp1 = temp0
	temp0 = max(prey[1], temp3)
	if temp0 != 0:
		temp1 = temp2 / temp0
	else:
		temp1 = temp0
	temp2 = prey[0] - temp2
	temp2 = prey[0] * temp2
	temp3 = prey[0] * temp3
	temp3 = temp2 + temp1
	temp5 = prey[0] * prey[0]
	temp5 = temp1 - temp0
	return [temp4, temp5]
