#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp1 = prey[0] - prey[1]
	if prey[0] != 0:
		temp1 = temp1 / prey[0]
	else:
		temp1 = prey[0]
	if temp1 != 0:
		temp0 = temp0 / temp1
	else:
		temp0 = temp1
	if temp0 != 0:
		temp0 = prey[0] % temp0
	else:
		temp0 = temp0
	temp0 = prey[0] * temp0
	temp1 = prey[0] * temp1
	temp2 = prey[1] * temp1
	if temp2 != 0:
		temp1 = prey[1] / temp2
	else:
		temp1 = temp2
	temp3 = temp0 - prey[0]
	temp0 = temp1 - temp3
	temp1 = min(prey[1], prey[0])
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = temp3 * temp1
	temp4 = temp3 + temp1
	temp2 = prey[0] * temp4
	temp4 = temp0 * temp4
	temp1 = min(temp4, temp4)
	temp1 = max(temp4, temp0)
	return [temp1, temp4]
