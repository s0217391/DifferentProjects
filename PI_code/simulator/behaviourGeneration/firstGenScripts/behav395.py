#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[0]
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	if temp0 > prey[0]:
		temp2 = -1 * temp0
	else:
		if prey[1] > prey[0]:
			temp2 = temp1 * prey[0]
		else:
			temp2 = min(prey[1], prey[1])
	temp2 = temp0 + prey[0]
	if temp1 != 0:
		temp3 = prey[1] / temp1
	else:
		temp3 = temp1
	temp1 = min(temp0, prey[1])
	temp2 = -1 * temp3
	temp2 = temp2 - temp2
	temp4 = prey[0] - temp1
	temp4 = max(prey[0], temp3)
	temp4 = max(prey[1], temp1)
	temp5 = max(prey[1], temp0)
	temp3 = temp5 - temp4
	temp1 = max(prey[0], temp2)
	if temp1 != 0:
		temp1 = temp4 / temp1
	else:
		temp1 = temp1
	if temp3 != 0:
		temp4 = prey[1] % temp3
	else:
		temp4 = temp3
	temp0 = min(temp5, temp5)
	temp3 = temp4 * temp0
	temp1 = max(temp0, temp5)
	temp4 = min(temp2, prey[1])
	temp5 = min(temp1, temp2)
	temp5 = temp5 - temp1
	temp2 = prey[0] + prey[0]
	temp5 = prey[1] - temp0
	temp2 = -1 * temp4
	return [temp0, temp3]