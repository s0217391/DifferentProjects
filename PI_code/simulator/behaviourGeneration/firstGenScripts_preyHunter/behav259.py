#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = -1 * temp0
	if temp2 != 0:
		temp0 = temp0 % temp2
	else:
		temp0 = temp2
	if temp2 != 0:
		temp3 = prey[1] / temp2
	else:
		temp3 = temp2
	temp2 = -1 * temp1
	temp3 = min(temp0, temp3)
	if temp2 != 0:
		temp4 = temp3 / temp2
	else:
		temp4 = temp2
	if temp1 > temp2:
		if temp4 > temp2:
			temp4 = prey[0] + temp3
		else:
			temp4 = temp1 - temp1
	else:
		temp4 = prey[1] * prey[0]
	temp0 = temp4 + temp2
	temp5 = temp3 * prey[0]
	if temp3 > prey[1]:
		temp1 = -1 * temp1
	else:
		temp1 = min(prey[0], temp4)
	temp1 = temp1 * temp0
	temp4 = -1 * temp3
	if prey[0] > prey[1]:
		if prey[0] != 0:
			temp3 = temp1 / prey[0]
		else:
			temp3 = prey[0]
	else:
		temp3 = temp4 * temp4
	if temp1 != 0:
		temp5 = temp2 % temp1
	else:
		temp5 = temp1
	if temp3 > prey[0]:
		if temp4 != 0:
			temp5 = prey[1] % temp4
		else:
			temp5 = temp4
	else:
		temp5 = max(prey[0], temp4)
	if temp3 != 0:
		temp5 = temp5 / temp3
	else:
		temp5 = temp3
	return [temp2, temp3]
