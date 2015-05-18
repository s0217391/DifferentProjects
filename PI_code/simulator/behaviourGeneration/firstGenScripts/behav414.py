#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	if prey[1] > prey[0]:
		temp0 = prey[1] * prey[0]
	else:
		temp0 = temp1 + prey[1]
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp2 = -1 * prey[1]
	if temp0 != 0:
		temp3 = temp0 % temp0
	else:
		temp3 = temp0
	if prey[1] > temp2:
		temp2 = max(temp0, temp3)
	else:
		if prey[1] != 0:
			temp2 = temp2 / prey[1]
		else:
			temp2 = prey[1]
	if temp0 != 0:
		temp3 = temp3 % temp0
	else:
		temp3 = temp0
	temp4 = -1 * temp3
	temp4 = prey[1] * temp3
	temp4 = temp3 + prey[1]
	temp3 = -1 * temp2
	temp2 = -1 * temp2
	temp5 = temp3 - temp3
	temp2 = -1 * temp3
	temp2 = max(temp5, temp1)
	temp4 = temp2 - temp5
	temp5 = -1 * prey[1]
	if temp0 != 0:
		temp1 = temp1 / temp0
	else:
		temp1 = temp0
	temp1 = min(temp0, temp0)
	if temp4 > temp4:
		temp1 = min(prey[1], temp5)
	else:
		temp1 = temp2 * temp0
	return [temp4, temp3]
