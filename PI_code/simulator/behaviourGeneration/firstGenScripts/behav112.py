#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	temp1 = temp0 - prey[1]
	temp1 = min(prey[0], temp1)
	if temp1 > temp0:
		temp1 = min(temp1, prey[0])
	else:
		temp1 = max(prey[0], temp1)
	temp0 = temp0 + temp1
	temp2 = max(temp1, temp0)
	temp2 = temp1 - prey[0]
	if prey[1] != 0:
		temp1 = temp1 / prey[1]
	else:
		temp1 = prey[1]
	temp3 = temp0 - prey[1]
	if temp3 != 0:
		temp4 = temp3 / temp3
	else:
		temp4 = temp3
	temp4 = prey[0] - prey[1]
	if temp2 > temp0:
		if temp3 != 0:
			temp2 = temp4 % temp3
		else:
			temp2 = temp3
	else:
		temp2 = min(prey[0], prey[0])
	temp5 = prey[0] - temp3
	temp1 = -1 * temp4
	temp0 = temp3 + temp0
	if temp1 != 0:
		temp4 = temp2 / temp1
	else:
		temp4 = temp1
	if temp0 != 0:
		temp2 = prey[0] / temp0
	else:
		temp2 = temp0
	temp5 = max(temp2, temp5)
	temp0 = temp5 - temp5
	temp2 = max(prey[1], temp0)
	temp0 = temp3 + temp4
	temp4 = max(temp0, temp0)
	return [prey[0], temp3]
