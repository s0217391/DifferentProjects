#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	if temp1 != 0:
		temp2 = prey[1] % temp1
	else:
		temp2 = temp1
	temp3 = temp0 * prey[0]
	temp4 = min(prey[0], temp0)
	if temp1 != 0:
		temp5 = temp1 % temp1
	else:
		temp5 = temp1
	if temp0 != 0:
		temp2 = prey[1] / temp0
	else:
		temp2 = temp0
	if temp1 > temp2:
		if prey[1] > temp1:
			if temp4 != 0:
				temp0 = temp2 % temp4
			else:
				temp0 = temp4
		else:
			if temp2 != 0:
				temp0 = temp1 / temp2
			else:
				temp0 = temp2
	else:
		temp0 = prey[1] + temp5
	temp4 = temp0 * prey[1]
	if prey[1] > prey[1]:
		if prey[0] != 0:
			temp2 = prey[0] % prey[0]
		else:
			temp2 = prey[0]
	else:
		temp2 = temp3 * temp3
	temp2 = max(temp2, temp0)
	temp6 = temp0 + temp5
	temp1 = max(temp5, temp1)
	temp4 = max(prey[1], temp2)
	temp7 = prey[1] - prey[1]
	temp0 = min(temp7, temp4)
	temp4 = prey[0] * temp3
	temp5 = temp2 * temp7
	temp7 = prey[0] - temp0
	if temp4 > temp4:
		temp1 = min(temp2, temp3)
	else:
		temp1 = temp2 - temp6
	temp0 = prey[1] * temp4
	temp6 = prey[1] * temp0
	temp6 = max(temp5, temp5)
	return [temp4, temp7]
