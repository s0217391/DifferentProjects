#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	temp1 = -1 * temp0
	temp2 = temp1 - temp0
	temp2 = max(temp1, temp2)
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp0 = max(prey[1], temp2)
	if temp1 > prey[1]:
		temp2 = temp2 * temp0
	else:
		temp2 = min(temp1, prey[0])
	temp1 = temp0 + temp2
	temp3 = temp1 * temp0
	temp4 = min(temp3, prey[0])
	temp3 = temp2 - temp4
	temp4 = temp4 + prey[0]
	temp1 = prey[0] - temp3
	temp0 = temp3 + temp4
	return [temp4, temp4]
