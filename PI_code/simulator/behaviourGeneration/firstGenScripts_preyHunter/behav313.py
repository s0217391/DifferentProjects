#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp0 = prey[0] * temp1
	temp2 = prey[0] * prey[1]
	temp3 = temp0 * prey[0]
	if temp2 != 0:
		temp0 = prey[1] / temp2
	else:
		temp0 = temp2
	if temp3 != 0:
		temp3 = temp2 / temp3
	else:
		temp3 = temp3
	if prey[1] != 0:
		temp3 = temp2 % prey[1]
	else:
		temp3 = prey[1]
	temp3 = max(temp0, temp2)
	temp0 = -1 * prey[0]
	temp3 = -1 * prey[1]
	if temp2 != 0:
		temp4 = temp2 % temp2
	else:
		temp4 = temp2
	temp5 = temp3 + prey[1]
	if temp4 > temp2:
		temp1 = min(temp2, temp0)
	else:
		if temp0 > prey[1]:
			temp1 = temp2 * temp2
		else:
			temp1 = max(temp3, temp0)
	temp1 = max(temp5, temp4)
	if temp1 != 0:
		temp2 = temp5 % temp1
	else:
		temp2 = temp1
	temp1 = min(temp3, temp5)
	return [temp0, temp3]
