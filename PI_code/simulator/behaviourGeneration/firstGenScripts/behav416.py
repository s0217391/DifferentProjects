#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[0]
	temp1 = temp0 + temp0
	temp2 = prey[1] + prey[0]
	temp1 = temp1 - temp1
	temp3 = min(temp0, prey[1])
	temp3 = -1 * temp0
	if temp1 > temp2:
		temp3 = temp3 - temp2
	else:
		temp3 = -1 * prey[0]
	if temp3 != 0:
		temp4 = prey[0] / temp3
	else:
		temp4 = temp3
	if temp2 != 0:
		temp2 = temp3 % temp2
	else:
		temp2 = temp2
	temp3 = temp4 - prey[1]
	if temp4 > temp2:
		if temp3 > temp2:
			temp0 = temp2 - prey[1]
		else:
			temp0 = temp0 + temp4
	else:
		if prey[0] != 0:
			temp0 = temp1 % prey[0]
		else:
			temp0 = prey[0]
	if temp0 != 0:
		temp3 = temp0 / temp0
	else:
		temp3 = temp0
	temp4 = -1 * temp3
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	temp1 = prey[1] - temp0
	temp2 = -1 * temp3
	temp0 = min(temp2, temp4)
	temp5 = max(prey[1], temp0)
	if temp5 > temp1:
		if temp3 != 0:
			temp3 = temp1 % temp3
		else:
			temp3 = temp3
	else:
		temp3 = prey[1] - temp3
	temp5 = min(prey[1], temp4)
	return [temp1, temp2]
