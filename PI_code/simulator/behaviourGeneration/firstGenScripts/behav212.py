#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	if temp0 > prey[0]:
		if temp0 != 0:
			temp1 = prey[1] % temp0
		else:
			temp1 = temp0
	else:
		if prey[0] != 0:
			temp1 = prey[1] / prey[0]
		else:
			temp1 = prey[0]
	temp2 = -1 * temp0
	temp3 = temp1 - temp2
	temp2 = temp0 + prey[1]
	if prey[0] > prey[1]:
		temp0 = temp3 - temp1
	else:
		temp0 = prey[1] * temp0
	temp1 = max(temp3, prey[0])
	temp1 = -1 * temp1
	temp1 = temp1 + temp3
	temp3 = min(prey[1], temp1)
	temp2 = temp3 - prey[0]
	if temp0 != 0:
		temp3 = temp3 % temp0
	else:
		temp3 = temp0
	if prey[1] > temp0:
		if temp1 > temp0:
			temp0 = min(temp1, temp1)
		else:
			temp0 = temp3 + temp1
	else:
		temp0 = -1 * temp0
	if prey[1] != 0:
		temp0 = temp3 % prey[1]
	else:
		temp0 = prey[1]
	temp2 = min(prey[0], temp3)
	return [prey[0], temp3]
