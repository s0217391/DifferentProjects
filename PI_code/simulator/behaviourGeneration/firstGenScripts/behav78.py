#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[1]
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = temp0 + prey[0]
	temp3 = temp0 - prey[0]
	temp1 = temp0 - prey[1]
	temp3 = temp2 + temp3
	temp4 = temp1 + prey[0]
	temp0 = max(temp1, temp4)
	if temp3 > temp1:
		temp0 = temp0 - temp3
	else:
		temp0 = -1 * temp1
	temp0 = min(prey[0], temp4)
	temp4 = temp0 + temp2
	if temp4 > temp2:
		temp0 = prey[0] + temp3
	else:
		temp0 = temp0 + temp4
	if prey[1] > prey[0]:
		temp2 = temp1 - temp4
	else:
		temp2 = min(temp2, temp1)
	if temp2 > prey[1]:
		temp1 = max(temp2, prey[0])
	else:
		temp1 = temp2 - temp4
	temp4 = temp1 - temp0
	if temp3 != 0:
		temp4 = prey[1] % temp3
	else:
		temp4 = temp3
	if temp0 > temp3:
		temp5 = -1 * temp4
	else:
		temp5 = max(temp3, temp1)
	if temp3 > temp3:
		temp2 = temp0 * temp3
	else:
		if temp5 > temp2:
			if prey[0] != 0:
				temp2 = temp2 % prey[0]
			else:
				temp2 = prey[0]
		else:
			if temp0 != 0:
				temp2 = temp5 / temp0
			else:
				temp2 = temp0
	temp0 = max(temp5, temp3)
	temp0 = max(temp4, temp3)
	temp1 = min(temp4, prey[0])
	return [temp4, temp4]
