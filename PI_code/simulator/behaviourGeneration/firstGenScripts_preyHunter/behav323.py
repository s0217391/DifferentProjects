#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = prey[0] - prey[1]
	else:
		temp0 = prey[1] * prey[1]
	temp1 = max(temp0, prey[1])
	temp2 = temp1 * temp1
	temp3 = -1 * temp0
	temp0 = prey[1] * temp3
	temp3 = min(temp3, prey[1])
	temp3 = temp2 + temp3
	if prey[0] > prey[0]:
		temp0 = -1 * temp1
	else:
		temp0 = temp3 - temp2
	temp4 = min(temp2, temp1)
	if temp4 != 0:
		temp4 = temp2 / temp4
	else:
		temp4 = temp4
	if temp1 > prey[0]:
		if prey[1] != 0:
			temp1 = prey[0] / prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = -1 * temp4
	temp5 = -1 * temp4
	temp4 = min(temp0, temp3)
	temp1 = temp5 - temp5
	temp4 = temp4 * temp4
	temp4 = max(prey[0], temp5)
	temp0 = -1 * temp5
	temp2 = temp4 + prey[1]
	temp4 = max(prey[0], temp5)
	temp1 = max(prey[0], temp4)
	if prey[1] > temp0:
		temp3 = min(temp3, prey[0])
	else:
		if temp1 != 0:
			temp3 = temp5 % temp1
		else:
			temp3 = temp1
	temp3 = -1 * temp0
	temp3 = prey[1] - temp0
	return [temp3, temp5]
