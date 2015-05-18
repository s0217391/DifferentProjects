#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	temp1 = max(prey[0], temp0)
	if temp1 != 0:
		temp2 = temp1 % temp1
	else:
		temp2 = temp1
	temp0 = temp0 - prey[1]
	temp3 = max(prey[0], temp2)
	temp3 = min(temp2, temp1)
	if prey[1] != 0:
		temp0 = temp2 / prey[1]
	else:
		temp0 = prey[1]
	temp0 = temp2 - prey[1]
	temp3 = prey[1] * prey[1]
	temp4 = temp3 * prey[1]
	temp1 = min(prey[1], temp3)
	if temp2 != 0:
		temp4 = temp3 / temp2
	else:
		temp4 = temp2
	temp3 = temp0 - prey[0]
	temp0 = min(prey[1], temp0)
	if temp2 != 0:
		temp0 = prey[1] / temp2
	else:
		temp0 = temp2
	if prey[0] > prey[1]:
		temp5 = -1 * temp1
	else:
		temp5 = -1 * temp4
	temp5 = max(temp3, temp5)
	temp5 = max(temp2, temp5)
	temp4 = temp1 * prey[0]
	temp1 = min(prey[1], temp0)
	temp2 = temp3 + temp0
	return [temp5, prey[1]]
