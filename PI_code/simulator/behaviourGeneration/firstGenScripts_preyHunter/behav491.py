#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	temp1 = -1 * prey[0]
	temp2 = min(temp1, prey[1])
	temp0 = temp1 - temp1
	temp3 = min(temp0, prey[1])
	temp0 = min(prey[1], prey[1])
	temp4 = -1 * temp0
	if temp3 > prey[0]:
		temp5 = min(temp4, prey[0])
	else:
		if prey[1] != 0:
			temp5 = temp3 / prey[1]
		else:
			temp5 = prey[1]
	temp2 = prey[0] * temp5
	if temp0 != 0:
		temp4 = temp5 / temp0
	else:
		temp4 = temp0
	temp0 = prey[1] * temp0
	if temp5 > temp4:
		temp6 = temp5 * temp0
	else:
		if temp1 != 0:
			temp6 = temp5 % temp1
		else:
			temp6 = temp1
	temp4 = min(temp0, temp4)
	temp7 = prey[1] - temp0
	if temp6 > temp3:
		temp3 = prey[0] - temp7
	else:
		temp3 = min(temp7, prey[1])
	temp2 = min(temp1, temp0)
	temp1 = -1 * temp4
	temp7 = temp5 * temp5
	if temp3 != 0:
		temp1 = temp7 / temp3
	else:
		temp1 = temp3
	temp2 = min(prey[1], prey[1])
	if temp6 != 0:
		temp1 = prey[0] / temp6
	else:
		temp1 = temp6
	temp3 = max(temp0, prey[0])
	temp2 = max(prey[1], temp3)
	return [temp1, temp4]
