#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = max(prey[0], prey[0])
	if prey[1] != 0:
		temp1 = temp1 / prey[1]
	else:
		temp1 = prey[1]
	temp2 = min(prey[1], prey[0])
	temp1 = prey[1] - prey[0]
	temp1 = temp1 * prey[0]
	temp2 = min(temp2, temp0)
	if prey[1] > temp2:
		temp1 = min(prey[0], temp2)
	else:
		if temp1 != 0:
			temp1 = prey[0] % temp1
		else:
			temp1 = temp1
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp3 = min(prey[0], temp0)
	if prey[0] != 0:
		temp3 = prey[1] % prey[0]
	else:
		temp3 = prey[0]
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp2 = temp1 % prey[0]
	else:
		temp2 = prey[0]
	temp0 = -1 * temp1
	temp1 = temp0 - temp2
	temp4 = -1 * temp0
	if temp2 > temp0:
		temp3 = prey[0] + temp4
	else:
		temp3 = temp1 + temp1
	temp1 = prey[1] - prey[1]
	if prey[1] != 0:
		temp3 = temp0 % prey[1]
	else:
		temp3 = prey[1]
	if temp0 != 0:
		temp0 = prey[1] % temp0
	else:
		temp0 = temp0
	temp2 = -1 * temp2
	temp5 = min(temp2, temp0)
	temp4 = prey[1] + temp5
	temp4 = temp4 - prey[1]
	temp2 = temp5 + temp2
	return [prey[0], temp1]
