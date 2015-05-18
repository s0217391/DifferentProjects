#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = -1 * prey[0]
	else:
		if prey[1] != 0:
			temp0 = prey[1] / prey[1]
		else:
			temp0 = prey[1]
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = prey[1] - prey[1]
	temp2 = prey[1] - temp2
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	temp3 = max(temp1, temp2)
	temp1 = temp1 + temp3
	if temp2 != 0:
		temp1 = temp2 / temp2
	else:
		temp1 = temp2
	if temp2 != 0:
		temp2 = prey[0] % temp2
	else:
		temp2 = temp2
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	if temp3 != 0:
		temp3 = temp1 / temp3
	else:
		temp3 = temp3
	temp1 = min(prey[1], temp1)
	if temp2 != 0:
		temp0 = prey[0] % temp2
	else:
		temp0 = temp2
	temp4 = -1 * temp2
	temp2 = temp2 - temp1
	temp4 = prey[0] - temp4
	temp0 = min(temp2, temp0)
	temp1 = max(prey[0], temp3)
	if temp0 != 0:
		temp3 = temp4 / temp0
	else:
		temp3 = temp0
	return [prey[1], temp4]
