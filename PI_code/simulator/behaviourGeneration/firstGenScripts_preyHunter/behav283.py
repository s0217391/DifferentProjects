#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	if prey[1] > temp0:
		temp1 = temp0 - prey[0]
	else:
		temp1 = min(prey[1], temp1)
	if temp1 > prey[0]:
		if temp0 != 0:
			temp2 = prey[0] % temp0
		else:
			temp2 = temp0
	else:
		if prey[0] != 0:
			temp2 = temp1 % prey[0]
		else:
			temp2 = prey[0]
	temp3 = max(temp2, temp2)
	if temp3 != 0:
		temp2 = prey[0] % temp3
	else:
		temp2 = temp3
	temp3 = min(prey[1], temp2)
	temp2 = min(prey[0], prey[0])
	temp2 = temp2 * prey[0]
	temp2 = temp2 + prey[1]
	temp2 = temp0 + prey[0]
	temp4 = temp2 - temp3
	temp3 = temp4 * temp3
	if prey[0] != 0:
		temp0 = temp2 / prey[0]
	else:
		temp0 = prey[0]
	temp3 = temp4 + prey[1]
	temp1 = temp0 * temp1
	temp4 = temp3 + temp1
	temp0 = min(temp3, temp1)
	return [prey[0], temp0]