#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = temp0 * temp0
	temp2 = min(prey[0], temp1)
	temp1 = temp1 + temp1
	if prey[1] > temp1:
		temp1 = prey[1] - temp2
	else:
		temp1 = max(temp1, temp1)
	temp0 = prey[1] + temp1
	if temp1 > temp1:
		temp3 = -1 * prey[1]
	else:
		temp3 = temp2 - temp0
	if temp0 != 0:
		temp3 = temp3 % temp0
	else:
		temp3 = temp0
	if temp0 > prey[1]:
		temp3 = -1 * temp1
	else:
		temp3 = min(temp2, prey[1])
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	if prey[0] != 0:
		temp2 = temp1 % prey[0]
	else:
		temp2 = prey[0]
	if temp1 != 0:
		temp3 = temp0 / temp1
	else:
		temp3 = temp1
	if temp0 > prey[0]:
		if temp2 != 0:
			temp4 = prey[0] % temp2
		else:
			temp4 = temp2
	else:
		if prey[1] > temp3:
			temp4 = temp3 - temp1
		else:
			temp4 = temp3 - prey[0]
	temp2 = temp0 - temp3
	temp5 = temp0 * prey[1]
	if temp3 != 0:
		temp2 = temp0 % temp3
	else:
		temp2 = temp3
	temp0 = max(temp0, prey[0])
	temp2 = max(temp5, temp0)
	return [temp2, prey[1]]
