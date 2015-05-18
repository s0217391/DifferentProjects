#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp0 + temp0
	temp0 = max(temp0, prey[0])
	temp0 = temp1 * temp1
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp0 = -1 * prey[1]
	temp2 = max(prey[0], temp0)
	temp3 = -1 * prey[1]
	temp0 = prey[0] - prey[1]
	temp3 = min(temp2, prey[1])
	if temp3 != 0:
		temp2 = temp2 % temp3
	else:
		temp2 = temp3
	temp4 = prey[0] + temp0
	temp0 = temp4 - prey[1]
	temp5 = min(temp1, prey[0])
	if prey[0] > prey[0]:
		temp5 = min(temp5, temp5)
	else:
		temp5 = max(temp0, prey[0])
	if prey[1] != 0:
		temp1 = temp5 % prey[1]
	else:
		temp1 = prey[1]
	temp3 = min(temp2, temp1)
	return [prey[0], prey[0]]
