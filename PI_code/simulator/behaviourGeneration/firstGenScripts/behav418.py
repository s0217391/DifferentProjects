#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = prey[0] + prey[0]
	else:
		temp0 = prey[0] * prey[0]
	temp1 = -1 * prey[0]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp0 = min(temp1, prey[1])
	temp2 = prey[0] * prey[0]
	if prey[1] != 0:
		temp3 = prey[1] % prey[1]
	else:
		temp3 = prey[1]
	temp3 = temp2 - temp3
	if prey[0] != 0:
		temp4 = prey[1] % prey[0]
	else:
		temp4 = prey[0]
	temp5 = min(temp2, temp4)
	temp0 = prey[1] * temp1
	if temp1 != 0:
		temp1 = prey[1] / temp1
	else:
		temp1 = temp1
	temp1 = max(temp5, temp2)
	temp5 = max(temp4, prey[0])
	temp2 = prey[1] * temp2
	temp3 = temp4 + temp2
	temp0 = prey[1] - prey[0]
	if temp0 > temp5:
		temp0 = -1 * temp5
	else:
		if temp1 != 0:
			temp0 = temp2 % temp1
		else:
			temp0 = temp1
	temp0 = -1 * temp2
	if prey[0] != 0:
		temp0 = temp1 % prey[0]
	else:
		temp0 = prey[0]
	if prey[1] > prey[0]:
		if temp3 > prey[0]:
			if prey[0] != 0:
				temp4 = prey[0] % prey[0]
			else:
				temp4 = prey[0]
		else:
			temp4 = prey[0] + temp5
	else:
		temp4 = -1 * temp4
	temp6 = temp5 * temp4
	temp2 = -1 * prey[1]
	temp1 = temp2 - temp2
	if prey[0] != 0:
		temp6 = temp5 % prey[0]
	else:
		temp6 = prey[0]
	return [temp5, temp4]
