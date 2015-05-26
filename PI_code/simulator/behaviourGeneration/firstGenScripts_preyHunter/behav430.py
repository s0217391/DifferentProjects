#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	if temp0 > prey[0]:
		temp1 = max(prey[0], temp0)
	else:
		temp1 = prey[0] - prey[1]
	if temp0 != 0:
		temp0 = temp1 / temp0
	else:
		temp0 = temp0
	if temp0 > prey[0]:
		temp1 = -1 * temp0
	else:
		temp1 = -1 * prey[0]
	temp2 = -1 * prey[1]
	temp3 = prey[0] * temp1
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	temp4 = temp0 + prey[1]
	if temp3 != 0:
		temp0 = temp4 % temp3
	else:
		temp0 = temp3
	temp4 = temp0 - temp4
	temp4 = max(temp1, temp0)
	temp2 = temp1 * temp4
	temp2 = min(prey[0], temp3)
	temp0 = -1 * temp2
	temp1 = -1 * temp3
	return [temp1, temp1]
