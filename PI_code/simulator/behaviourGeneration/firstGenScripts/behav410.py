#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = -1 * prey[0]
	temp0 = min(prey[0], prey[0])
	temp2 = max(temp0, prey[1])
	temp3 = min(prey[1], temp0)
	temp1 = temp0 * prey[1]
	if temp3 != 0:
		temp1 = temp3 % temp3
	else:
		temp1 = temp3
	if temp0 != 0:
		temp4 = temp3 % temp0
	else:
		temp4 = temp0
	if temp4 != 0:
		temp4 = temp0 % temp4
	else:
		temp4 = temp4
	temp1 = temp2 - temp2
	temp5 = temp0 * temp1
	temp1 = temp5 - temp2
	if temp5 > temp4:
		temp5 = temp3 * prey[0]
	else:
		if temp5 > temp1:
			temp5 = min(temp1, prey[0])
		else:
			if prey[1] != 0:
				temp5 = temp4 % prey[1]
			else:
				temp5 = prey[1]
	if prey[0] != 0:
		temp4 = temp0 % prey[0]
	else:
		temp4 = prey[0]
	if temp3 != 0:
		temp4 = temp4 % temp3
	else:
		temp4 = temp3
	temp6 = -1 * temp4
	temp6 = temp1 * temp6
	if temp5 > prey[0]:
		if temp1 > temp2:
			temp3 = temp3 + temp5
		else:
			if temp4 != 0:
				temp3 = prey[0] / temp4
			else:
				temp3 = temp4
	else:
		temp3 = temp6 * prey[0]
	if temp6 != 0:
		temp1 = temp6 / temp6
	else:
		temp1 = temp6
	if prey[1] != 0:
		temp7 = prey[1] % prey[1]
	else:
		temp7 = prey[1]
	temp2 = temp7 * prey[1]
	return [prey[1], prey[1]]