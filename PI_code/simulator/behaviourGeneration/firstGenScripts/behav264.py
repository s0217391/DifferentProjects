#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		if prey[0] != 0:
			temp0 = prey[1] % prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = prey[1] + prey[0]
	temp1 = -1 * prey[1]
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = temp1 - temp1
	temp0 = temp2 * temp2
	if temp0 != 0:
		temp3 = temp1 % temp0
	else:
		temp3 = temp0
	temp4 = temp3 + temp3
	if temp2 != 0:
		temp3 = temp4 % temp2
	else:
		temp3 = temp2
	temp3 = temp1 - temp0
	temp1 = -1 * temp3
	temp1 = temp1 * temp0
	if temp3 > prey[0]:
		temp2 = temp1 - temp2
	else:
		temp2 = max(temp3, temp3)
	temp1 = temp1 - prey[1]
	temp4 = temp0 * temp1
	temp4 = temp1 + temp3
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp0 = min(prey[0], temp2)
	if temp2 != 0:
		temp5 = temp4 / temp2
	else:
		temp5 = temp2
	if temp1 != 0:
		temp5 = temp3 / temp1
	else:
		temp5 = temp1
	if prey[0] > temp2:
		if temp1 > temp3:
			temp4 = temp0 - temp0
		else:
			temp4 = -1 * prey[0]
	else:
		temp4 = prey[0] + temp1
	return [temp0, temp1]
