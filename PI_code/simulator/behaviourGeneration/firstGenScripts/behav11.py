#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	temp2 = -1 * temp1
	temp2 = min(temp1, temp1)
	temp2 = temp1 - temp2
	temp0 = prey[1] + temp2
	temp3 = temp0 * temp0
	temp4 = temp0 - temp0
	if temp3 != 0:
		temp4 = temp1 / temp3
	else:
		temp4 = temp3
	if temp3 != 0:
		temp2 = prey[1] / temp3
	else:
		temp2 = temp3
	temp4 = -1 * temp0
	temp1 = temp1 * prey[1]
	if temp3 != 0:
		temp0 = temp0 / temp3
	else:
		temp0 = temp3
	temp2 = prey[0] + temp0
	if temp4 != 0:
		temp2 = prey[1] / temp4
	else:
		temp2 = temp4
	temp3 = -1 * temp2
	return [temp1, temp0]
