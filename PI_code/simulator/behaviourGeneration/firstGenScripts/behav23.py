#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	if temp0 != 0:
		temp0 = temp0 / temp0
	else:
		temp0 = temp0
	if prey[1] > temp1:
		if temp1 != 0:
			temp0 = temp0 / temp1
		else:
			temp0 = temp1
	else:
		if prey[1] != 0:
			temp0 = prey[1] % prey[1]
		else:
			temp0 = prey[1]
	temp2 = -1 * prey[0]
	if prey[0] != 0:
		temp3 = prey[0] % prey[0]
	else:
		temp3 = prey[0]
	temp4 = max(temp0, temp3)
	temp1 = min(temp0, temp1)
	if prey[0] != 0:
		temp2 = temp0 % prey[0]
	else:
		temp2 = prey[0]
	temp2 = min(temp4, temp0)
	temp0 = -1 * temp1
	temp2 = temp1 * prey[1]
	if temp2 != 0:
		temp4 = temp0 / temp2
	else:
		temp4 = temp2
	temp4 = -1 * temp3
	temp2 = max(temp4, temp1)
	if temp3 != 0:
		temp4 = temp2 / temp3
	else:
		temp4 = temp3
	temp5 = prey[1] + temp2
	temp4 = min(prey[0], temp0)
	temp0 = temp0 - temp4
	temp0 = max(temp0, temp5)
	temp5 = prey[1] + temp4
	temp3 = min(temp3, prey[1])
	temp1 = temp5 * temp3
	temp4 = temp1 + temp2
	if temp3 != 0:
		temp0 = temp4 % temp3
	else:
		temp0 = temp3
	return [temp2, temp0]
