#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[1]
	temp1 = min(prey[0], prey[0])
	if temp1 != 0:
		temp2 = temp1 % temp1
	else:
		temp2 = temp1
	temp0 = min(prey[1], temp0)
	temp3 = prey[0] * temp2
	if temp1 > temp2:
		temp0 = prey[0] - temp3
	else:
		temp0 = temp0 * temp3
	temp1 = temp1 + prey[1]
	temp2 = -1 * prey[0]
	temp3 = temp2 + prey[0]
	temp4 = temp3 - temp3
	temp0 = max(temp3, temp0)
	temp5 = -1 * temp0
	temp1 = temp0 - temp3
	if temp4 != 0:
		temp0 = temp3 % temp4
	else:
		temp0 = temp4
	temp3 = temp0 + temp3
	if prey[1] > temp2:
		temp4 = max(prey[0], temp2)
	else:
		temp4 = temp2 * temp2
	if temp0 != 0:
		temp4 = temp5 / temp0
	else:
		temp4 = temp0
	return [prey[0], temp5]
