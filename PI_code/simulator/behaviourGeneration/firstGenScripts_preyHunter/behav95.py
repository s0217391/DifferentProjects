#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	temp1 = -1 * temp0
	temp2 = prey[1] + prey[1]
	if temp0 != 0:
		temp3 = prey[0] % temp0
	else:
		temp3 = temp0
	if temp2 != 0:
		temp0 = prey[0] % temp2
	else:
		temp0 = temp2
	if temp1 > prey[1]:
		if temp0 > prey[1]:
			temp1 = -1 * temp2
		else:
			temp1 = max(temp3, temp3)
	else:
		if prey[0] != 0:
			temp1 = temp2 / prey[0]
		else:
			temp1 = prey[0]
	if temp1 != 0:
		temp4 = prey[0] / temp1
	else:
		temp4 = temp1
	temp4 = prey[1] + temp2
	if temp4 != 0:
		temp1 = temp2 % temp4
	else:
		temp1 = temp4
	temp1 = -1 * temp0
	temp3 = -1 * temp2
	if temp1 != 0:
		temp1 = temp3 / temp1
	else:
		temp1 = temp1
	temp5 = temp2 * temp0
	if temp3 > prey[1]:
		temp3 = max(prey[0], temp1)
	else:
		temp3 = prey[1] + temp4
	if temp4 > temp4:
		if temp0 != 0:
			temp0 = temp1 / temp0
		else:
			temp0 = temp0
	else:
		if prey[0] != 0:
			temp0 = temp2 / prey[0]
		else:
			temp0 = prey[0]
	return [temp4, temp1]
