#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	temp1 = temp0 - prey[0]
	temp1 = max(prey[1], temp1)
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	if prey[1] != 0:
		temp1 = prey[1] / prey[1]
	else:
		temp1 = prey[1]
	if temp0 != 0:
		temp2 = prey[0] / temp0
	else:
		temp2 = temp0
	if prey[0] > prey[0]:
		temp1 = prey[1] * temp2
	else:
		temp1 = prey[1] * temp1
	if temp2 > temp0:
		temp0 = -1 * temp2
	else:
		temp0 = prey[0] - prey[0]
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	if temp3 != 0:
		temp4 = prey[1] % temp3
	else:
		temp4 = temp3
	temp0 = max(temp4, prey[1])
	temp0 = max(temp1, prey[1])
	temp2 = -1 * temp0
	if temp2 > temp2:
		if prey[1] > temp0:
			if temp1 != 0:
				temp5 = prey[0] % temp1
			else:
				temp5 = temp1
		else:
			if temp1 != 0:
				temp5 = prey[1] / temp1
			else:
				temp5 = temp1
	else:
		temp5 = -1 * temp1
	temp3 = temp3 * temp1
	temp0 = min(prey[1], prey[1])
	temp4 = temp3 - temp1
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	temp6 = temp4 + temp4
	if temp0 != 0:
		temp5 = temp0 / temp0
	else:
		temp5 = temp0
	temp7 = min(temp1, temp2)
	temp4 = temp0 * prey[0]
	temp7 = max(temp2, temp3)
	return [temp6, temp6]
