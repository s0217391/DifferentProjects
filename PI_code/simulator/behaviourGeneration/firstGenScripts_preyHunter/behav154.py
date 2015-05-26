#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp1 = temp1 * temp1
	temp2 = min(temp0, prey[1])
	temp0 = min(prey[1], temp2)
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp2 = max(prey[0], prey[0])
	if temp2 != 0:
		temp2 = temp1 % temp2
	else:
		temp2 = temp2
	temp1 = min(temp2, temp0)
	temp1 = temp0 * temp1
	temp2 = prey[0] - temp1
	temp0 = min(temp2, temp2)
	temp0 = min(temp0, prey[1])
	if temp1 != 0:
		temp2 = temp1 / temp1
	else:
		temp2 = temp1
	temp0 = min(temp2, temp2)
	if temp1 > temp1:
		temp3 = prey[0] + temp0
	else:
		temp3 = temp1 + temp1
	temp3 = temp2 * temp1
	temp0 = min(temp1, temp2)
	if prey[1] != 0:
		temp3 = prey[0] % prey[1]
	else:
		temp3 = prey[1]
	temp4 = max(temp3, temp1)
	temp1 = max(prey[1], temp1)
	temp0 = min(temp1, temp0)
	temp2 = temp2 - temp2
	temp5 = temp0 * temp1
	temp6 = -1 * prey[1]
	return [prey[0], temp2]
