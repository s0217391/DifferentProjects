#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	temp1 = min(temp0, temp0)
	if prey[1] > prey[0]:
		temp1 = max(prey[1], temp0)
	else:
		temp1 = temp0 - temp1
	if prey[0] != 0:
		temp2 = prey[0] % prey[0]
	else:
		temp2 = prey[0]
	temp2 = temp0 * prey[1]
	if temp1 != 0:
		temp3 = prey[1] / temp1
	else:
		temp3 = temp1
	temp1 = temp1 - temp1
	if prey[1] > temp0:
		if temp3 != 0:
			temp0 = prey[0] % temp3
		else:
			temp0 = temp3
	else:
		temp0 = max(prey[0], prey[0])
	temp4 = max(temp2, temp0)
	if prey[0] != 0:
		temp4 = temp4 / prey[0]
	else:
		temp4 = prey[0]
	temp5 = temp0 - prey[1]
	if prey[1] != 0:
		temp5 = temp2 % prey[1]
	else:
		temp5 = prey[1]
	temp5 = temp1 + temp4
	temp5 = max(temp0, temp2)
	if temp4 != 0:
		temp4 = prey[0] % temp4
	else:
		temp4 = temp4
	if temp4 > temp5:
		temp0 = prey[0] - temp3
	else:
		if temp1 != 0:
			temp0 = temp4 % temp1
		else:
			temp0 = temp1
	return [prey[0], temp1]
