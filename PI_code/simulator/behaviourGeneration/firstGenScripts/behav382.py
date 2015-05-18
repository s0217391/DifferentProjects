#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = temp0 * prey[1]
	temp0 = prey[1] * temp1
	temp2 = temp1 + temp0
	temp3 = min(temp0, prey[1])
	if prey[1] != 0:
		temp4 = prey[0] % prey[1]
	else:
		temp4 = prey[1]
	temp1 = max(temp1, temp3)
	temp2 = temp4 + temp1
	temp4 = min(temp2, prey[1])
	temp4 = -1 * temp0
	temp5 = temp3 + prey[1]
	temp0 = temp0 + temp0
	temp3 = max(temp3, temp4)
	temp0 = max(temp1, temp1)
	return [temp5, temp5]
