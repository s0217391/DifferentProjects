#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[1]
	temp1 = min(temp0, temp0)
	temp2 = temp0 * prey[0]
	temp3 = -1 * temp0
	temp0 = temp1 + temp2
	if prey[0] != 0:
		temp3 = prey[1] / prey[0]
	else:
		temp3 = prey[0]
	if prey[0] > prey[1]:
		if temp2 != 0:
			temp4 = temp1 % temp2
		else:
			temp4 = temp2
	else:
		temp4 = temp3 - temp1
	temp3 = temp1 + temp4
	temp5 = temp2 * temp2
	temp5 = max(prey[1], temp0)
	if temp2 != 0:
		temp3 = temp3 % temp2
	else:
		temp3 = temp2
	if temp3 > temp2:
		if temp2 != 0:
			temp2 = temp3 % temp2
		else:
			temp2 = temp2
	else:
		temp2 = temp0 - prey[0]
	if prey[0] > prey[0]:
		if temp4 > temp4:
			temp2 = temp5 - temp1
		else:
			if temp2 > prey[1]:
				temp2 = min(temp1, temp4)
			else:
				if temp5 != 0:
					temp2 = temp1 % temp5
				else:
					temp2 = temp5
	else:
		temp2 = max(temp1, temp2)
	temp1 = temp3 * prey[0]
	temp0 = temp3 - temp2
	return [temp4, temp3]
