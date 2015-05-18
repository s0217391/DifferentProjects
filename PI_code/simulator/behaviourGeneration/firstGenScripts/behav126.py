#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[0]
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	if temp1 > prey[1]:
		temp1 = prey[1] - prey[0]
	else:
		if prey[1] != 0:
			temp1 = temp0 / prey[1]
		else:
			temp1 = prey[1]
	temp2 = temp0 - prey[0]
	temp0 = max(temp0, temp2)
	if temp2 != 0:
		temp1 = temp0 / temp2
	else:
		temp1 = temp2
	if temp0 != 0:
		temp2 = temp1 / temp0
	else:
		temp2 = temp0
	if temp0 != 0:
		temp2 = prey[1] % temp0
	else:
		temp2 = temp0
	temp1 = prey[0] + prey[0]
	temp1 = min(prey[1], temp0)
	temp2 = -1 * prey[0]
	temp0 = temp0 - temp2
	if temp1 != 0:
		temp1 = temp1 % temp1
	else:
		temp1 = temp1
	temp3 = -1 * prey[1]
	temp2 = max(temp2, prey[1])
	temp2 = -1 * temp0
	temp0 = temp2 + prey[1]
	temp2 = temp0 - temp0
	temp2 = max(temp0, temp3)
	temp0 = temp3 - prey[1]
	temp4 = temp1 + temp0
	temp4 = max(prey[0], prey[0])
	temp1 = -1 * temp4
	return [temp1, temp0]
