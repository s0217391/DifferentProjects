#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = min(prey[0], prey[0])
	else:
		if prey[0] != 0:
			temp0 = prey[0] % prey[0]
		else:
			temp0 = prey[0]
	if prey[0] > temp0:
		if temp0 != 0:
			temp1 = prey[0] / temp0
		else:
			temp1 = temp0
	else:
		temp1 = min(prey[0], prey[0])
	if temp1 != 0:
		temp0 = temp1 % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp2 = temp0 % prey[0]
	else:
		temp2 = prey[0]
	temp2 = max(temp0, temp2)
	if temp1 != 0:
		temp3 = prey[1] / temp1
	else:
		temp3 = temp1
	temp3 = -1 * prey[0]
	if temp0 != 0:
		temp3 = temp1 % temp0
	else:
		temp3 = temp0
	temp4 = -1 * temp2
	temp1 = max(temp3, prey[1])
	if temp1 != 0:
		temp3 = temp1 % temp1
	else:
		temp3 = temp1
	temp5 = max(temp3, temp1)
	temp0 = temp2 - temp2
	if temp0 != 0:
		temp6 = temp5 / temp0
	else:
		temp6 = temp0
	if temp5 > temp6:
		if temp4 > prey[0]:
			if temp2 > temp3:
				if temp5 > temp6:
					temp6 = temp1 + temp1
				else:
					temp6 = min(temp1, temp1)
			else:
				temp6 = prey[0] - temp1
		else:
			if temp2 != 0:
				temp6 = temp3 % temp2
			else:
				temp6 = temp2
	else:
		if temp4 > prey[1]:
			if temp3 != 0:
				temp6 = temp5 / temp3
			else:
				temp6 = temp3
		else:
			temp6 = temp5 * temp5
	if prey[0] != 0:
		temp4 = temp6 % prey[0]
	else:
		temp4 = prey[0]
	temp4 = max(temp0, temp3)
	if temp0 != 0:
		temp2 = temp5 / temp0
	else:
		temp2 = temp0
	if temp2 != 0:
		temp0 = temp6 / temp2
	else:
		temp0 = temp2
	temp0 = max(temp0, temp2)
	if temp3 != 0:
		temp7 = temp1 % temp3
	else:
		temp7 = temp3
	return [prey[1], prey[0]]
