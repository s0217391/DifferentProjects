#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = min(temp0, temp0)
	temp1 = max(temp1, prey[1])
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	temp1 = -1 * temp1
	temp2 = temp1 * prey[1]
	if temp0 > temp2:
		temp2 = prey[0] * prey[1]
	else:
		if prey[1] != 0:
			temp2 = temp2 % prey[1]
		else:
			temp2 = prey[1]
	temp3 = temp1 - prey[0]
	if temp1 != 0:
		temp4 = prey[0] / temp1
	else:
		temp4 = temp1
	temp0 = temp1 - temp1
	if temp0 != 0:
		temp4 = prey[0] / temp0
	else:
		temp4 = temp0
	temp5 = min(temp3, prey[1])
	temp1 = temp3 + temp1
	temp5 = temp4 * temp5
	if prey[1] > prey[0]:
		temp3 = max(temp4, temp2)
	else:
		if temp2 != 0:
			temp3 = temp2 / temp2
		else:
			temp3 = temp2
	temp1 = prey[1] * temp5
	temp5 = -1 * prey[1]
	temp1 = temp3 * temp1
	if prey[1] != 0:
		temp1 = temp2 / prey[1]
	else:
		temp1 = prey[1]
	temp6 = max(temp5, temp0)
	if temp3 > temp2:
		if temp4 != 0:
			temp5 = temp2 % temp4
		else:
			temp5 = temp4
	else:
		temp5 = max(temp0, temp0)
	return [temp3, temp3]
