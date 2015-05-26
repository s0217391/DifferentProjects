#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	temp1 = max(prey[1], temp0)
	temp2 = temp0 + temp0
	temp2 = -1 * prey[0]
	temp3 = prey[1] * temp0
	temp0 = temp2 * prey[0]
	temp0 = temp1 * temp2
	temp4 = prey[1] * prey[0]
	temp2 = min(temp4, prey[0])
	temp5 = -1 * temp0
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	temp3 = temp0 - temp1
	if temp4 > temp2:
		temp1 = min(prey[1], temp1)
	else:
		if prey[0] > temp0:
			if temp2 > temp1:
				temp1 = temp5 * temp4
			else:
				if prey[0] > prey[0]:
					temp1 = temp2 - prey[1]
				else:
					temp1 = prey[1] - temp3
		else:
			if prey[0] > temp3:
				temp1 = temp1 + prey[1]
			else:
				temp1 = min(prey[0], temp2)
	temp3 = prey[0] - temp1
	temp4 = -1 * temp0
	temp3 = temp1 * prey[1]
	temp6 = temp3 - prey[1]
	temp7 = -1 * prey[1]
	if temp3 != 0:
		temp5 = temp4 % temp3
	else:
		temp5 = temp3
	if prey[0] != 0:
		temp6 = temp2 % prey[0]
	else:
		temp6 = prey[0]
	if temp4 != 0:
		temp0 = temp7 % temp4
	else:
		temp0 = temp4
	temp4 = min(temp3, temp2)
	temp1 = temp1 * temp6
	if temp1 > temp5:
		temp1 = min(temp1, temp1)
	else:
		temp1 = temp3 * temp5
	return [prey[1], temp7]
