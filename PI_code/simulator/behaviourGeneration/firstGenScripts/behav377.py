#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[1] - prey[0]
	temp2 = prey[0] + prey[0]
	if prey[0] > temp1:
		temp3 = max(temp1, prey[0])
	else:
		if temp0 != 0:
			temp3 = temp2 % temp0
		else:
			temp3 = temp0
	temp2 = max(temp1, prey[1])
	if prey[1] > temp0:
		if prey[0] > temp1:
			if temp1 != 0:
				temp1 = temp2 / temp1
			else:
				temp1 = temp1
		else:
			temp1 = temp1 - temp1
	else:
		temp1 = max(prey[1], temp0)
	temp4 = max(temp3, temp1)
	if temp4 != 0:
		temp3 = prey[1] / temp4
	else:
		temp3 = temp4
	temp4 = min(temp2, temp0)
	temp4 = max(temp0, temp0)
	if temp1 > temp3:
		temp5 = max(temp2, temp2)
	else:
		if temp1 != 0:
			temp5 = temp4 % temp1
		else:
			temp5 = temp1
	temp5 = temp5 - temp5
	temp6 = temp1 + temp5
	temp0 = temp4 - temp0
	temp0 = -1 * temp4
	if temp6 > temp0:
		temp3 = temp1 - temp6
	else:
		if temp1 > temp3:
			temp3 = temp0 * temp6
		else:
			temp3 = temp5 - temp0
	temp2 = prey[0] * temp5
	if temp5 != 0:
		temp5 = temp1 % temp5
	else:
		temp5 = temp5
	return [temp0, temp1]