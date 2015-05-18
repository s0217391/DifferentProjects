#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp2 = max(prey[0], temp1)
	if temp0 > temp2:
		temp3 = -1 * prey[1]
	else:
		temp3 = min(temp0, temp0)
	temp4 = prey[0] - temp2
	temp1 = -1 * prey[1]
	if temp3 > temp1:
		temp3 = max(temp0, prey[1])
	else:
		temp3 = max(temp2, temp1)
	temp0 = temp1 - temp0
	temp4 = max(prey[1], temp1)
	temp4 = -1 * temp2
	temp5 = temp0 - prey[1]
	if temp2 != 0:
		temp4 = prey[0] / temp2
	else:
		temp4 = temp2
	temp3 = -1 * temp3
	temp2 = temp0 + temp4
	return [temp3, temp4]
