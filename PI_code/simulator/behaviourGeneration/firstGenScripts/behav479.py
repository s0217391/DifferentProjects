#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[0]:
		if prey[1] != 0:
			temp0 = prey[1] / prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = prey[0] + prey[0]
	temp1 = prey[0] * temp0
	temp0 = prey[0] + prey[1]
	temp0 = prey[1] * temp1
	temp1 = prey[0] + temp0
	temp1 = temp0 + temp1
	temp2 = temp1 - prey[1]
	if temp2 != 0:
		temp2 = temp2 / temp2
	else:
		temp2 = temp2
	temp3 = max(prey[1], prey[0])
	if prey[0] > temp0:
		temp1 = -1 * prey[0]
	else:
		temp1 = temp2 - prey[0]
	if prey[0] != 0:
		temp4 = temp2 / prey[0]
	else:
		temp4 = prey[0]
	temp1 = temp1 + prey[1]
	temp5 = max(temp1, temp1)
	temp2 = -1 * temp1
	temp5 = temp5 * prey[1]
	temp1 = temp2 * prey[1]
	temp1 = max(prey[1], temp5)
	if temp5 > temp4:
		temp4 = max(temp3, temp5)
	else:
		if temp2 != 0:
			temp4 = temp3 / temp2
		else:
			temp4 = temp2
	temp5 = temp4 + temp1
	if temp4 != 0:
		temp5 = temp1 / temp4
	else:
		temp5 = temp4
	if temp5 != 0:
		temp6 = temp1 % temp5
	else:
		temp6 = temp5
	temp4 = temp6 + temp5
	if temp1 > temp1:
		if prey[1] > temp5:
			temp2 = temp0 - temp6
		else:
			if prey[1] > prey[1]:
				if temp6 != 0:
					temp2 = temp5 % temp6
				else:
					temp2 = temp6
			else:
				temp2 = prey[1] + temp0
	else:
		temp2 = -1 * temp2
	if temp6 > temp4:
		temp7 = max(temp4, temp6)
	else:
		temp7 = -1 * temp3
	temp7 = -1 * temp2
	return [temp5, temp6]
