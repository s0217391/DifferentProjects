#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	if prey[0] > prey[1]:
		temp1 = prey[1] + prey[0]
	else:
		temp1 = max(prey[1], temp0)
	temp2 = max(temp0, temp0)
	temp1 = temp1 - temp2
	temp3 = -1 * temp2
	temp0 = max(temp2, temp1)
	temp1 = temp0 - prey[1]
	temp4 = min(temp0, temp0)
	if temp2 != 0:
		temp0 = prey[0] % temp2
	else:
		temp0 = temp2
	temp3 = prey[0] + temp1
	if temp4 != 0:
		temp2 = temp4 % temp4
	else:
		temp2 = temp4
	temp2 = max(prey[0], temp1)
	temp3 = prey[1] - prey[1]
	temp5 = -1 * temp1
	temp6 = -1 * prey[1]
	return [temp4, temp0]
