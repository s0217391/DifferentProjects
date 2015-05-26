#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = temp0 * prey[1]
	if temp0 > prey[1]:
		temp2 = temp0 - temp0
	else:
		if temp1 != 0:
			temp2 = prey[0] / temp1
		else:
			temp2 = temp1
	temp3 = -1 * temp0
	temp4 = max(temp2, temp0)
	temp3 = -1 * temp0
	temp5 = max(temp1, prey[0])
	temp4 = min(temp2, temp5)
	temp4 = max(prey[0], temp0)
	temp0 = temp3 * temp3
	if temp0 > temp5:
		temp3 = prey[1] - temp0
	else:
		temp3 = -1 * prey[0]
	temp4 = temp4 - temp1
	temp3 = max(temp0, prey[0])
	temp2 = min(temp1, temp2)
	temp6 = temp5 * temp5
	if temp4 != 0:
		temp6 = temp5 / temp4
	else:
		temp6 = temp4
	temp4 = min(temp1, temp2)
	if prey[1] > prey[1]:
		temp7 = -1 * temp5
	else:
		if temp3 != 0:
			temp7 = temp5 / temp3
		else:
			temp7 = temp3
	temp3 = -1 * temp7
	temp0 = min(temp0, temp4)
	return [temp0, temp5]
