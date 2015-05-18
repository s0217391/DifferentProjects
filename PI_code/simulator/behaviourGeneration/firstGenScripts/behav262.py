#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if temp0 > prey[0]:
		temp1 = max(prey[0], prey[0])
	else:
		temp1 = temp0 + temp0
	temp2 = max(prey[0], temp1)
	temp1 = max(temp2, temp0)
	temp3 = -1 * temp1
	if temp0 != 0:
		temp2 = temp1 % temp0
	else:
		temp2 = temp0
	temp1 = -1 * temp3
	temp3 = temp2 * temp0
	if temp2 != 0:
		temp3 = temp1 % temp2
	else:
		temp3 = temp2
	if temp3 != 0:
		temp2 = temp3 % temp3
	else:
		temp2 = temp3
	temp4 = prey[1] - temp2
	temp4 = temp2 + temp0
	return [temp0, prey[1]]
