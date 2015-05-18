#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = min(prey[0], prey[0])
	else:
		temp0 = prey[1] - prey[0]
	temp1 = prey[0] - temp0
	if temp0 != 0:
		temp1 = temp1 / temp0
	else:
		temp1 = temp0
	temp2 = prey[0] - temp1
	temp3 = temp0 + temp2
	temp1 = min(prey[0], prey[0])
	temp3 = min(prey[1], temp0)
	temp3 = max(temp1, temp3)
	if prey[0] > temp2:
		if prey[1] != 0:
			temp3 = temp0 % prey[1]
		else:
			temp3 = prey[1]
	else:
		temp3 = temp3 * temp3
	temp3 = prey[0] + prey[0]
	temp4 = max(temp2, temp0)
	temp3 = prey[0] - temp3
	temp0 = -1 * temp3
	if temp2 > prey[0]:
		temp0 = temp2 - temp0
	else:
		if prey[1] != 0:
			temp0 = temp4 % prey[1]
		else:
			temp0 = prey[1]
	if prey[0] != 0:
		temp2 = temp3 % prey[0]
	else:
		temp2 = prey[0]
	temp0 = temp4 + prey[1]
	temp0 = min(temp4, prey[0])
	if temp4 > prey[0]:
		temp5 = -1 * temp0
	else:
		if temp0 != 0:
			temp5 = temp3 % temp0
		else:
			temp5 = temp0
	temp5 = -1 * temp1
	temp6 = min(temp5, temp1)
	return [temp1, prey[0]]
