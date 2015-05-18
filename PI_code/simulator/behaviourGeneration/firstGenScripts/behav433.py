#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[1] - prey[1]
	temp2 = prey[0] - prey[1]
	if prey[0] > temp1:
		temp2 = temp1 * prey[1]
	else:
		temp2 = prey[1] - temp2
	temp3 = max(temp1, temp1)
	if temp0 != 0:
		temp3 = prey[0] % temp0
	else:
		temp3 = temp0
	if prey[0] != 0:
		temp1 = temp3 / prey[0]
	else:
		temp1 = prey[0]
	if temp1 > prey[1]:
		temp0 = max(temp1, prey[1])
	else:
		if temp0 != 0:
			temp0 = prey[1] / temp0
		else:
			temp0 = temp0
	temp4 = -1 * prey[0]
	if temp1 != 0:
		temp2 = temp4 % temp1
	else:
		temp2 = temp1
	temp1 = prey[1] + temp1
	if prey[0] != 0:
		temp5 = temp2 % prey[0]
	else:
		temp5 = prey[0]
	temp6 = temp3 * temp0
	if temp0 > prey[1]:
		temp3 = temp3 - temp1
	else:
		temp3 = max(temp0, temp0)
	temp4 = prey[1] * temp6
	if temp4 != 0:
		temp7 = prey[0] % temp4
	else:
		temp7 = temp4
	return [prey[0], temp7]
