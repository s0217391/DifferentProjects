#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = -1 * temp0
	temp1 = prey[1] - temp0
	temp0 = temp1 + prey[0]
	if temp1 > temp0:
		if temp0 != 0:
			temp1 = temp0 % temp0
		else:
			temp1 = temp0
	else:
		temp1 = max(prey[0], temp0)
	if prey[0] != 0:
		temp2 = temp0 / prey[0]
	else:
		temp2 = prey[0]
	temp2 = max(prey[0], prey[0])
	temp2 = temp1 * temp0
	temp3 = temp0 - temp2
	if temp2 > temp2:
		temp4 = -1 * temp2
	else:
		temp4 = temp3 + prey[0]
	temp2 = temp3 + temp1
	temp3 = max(prey[1], prey[0])
	if temp2 > temp0:
		temp3 = temp3 - temp3
	else:
		temp3 = prey[1] * temp4
	temp3 = temp0 * temp0
	temp0 = temp4 * temp0
	if temp1 > temp2:
		if prey[1] > temp1:
			temp1 = -1 * temp1
		else:
			temp1 = -1 * temp3
	else:
		temp1 = -1 * prey[0]
	temp4 = prey[1] * temp3
	temp0 = min(temp2, prey[0])
	if prey[1] > temp2:
		temp3 = max(temp4, prey[0])
	else:
		temp3 = prey[1] + temp2
	if prey[0] > temp0:
		temp4 = temp0 - temp0
	else:
		temp4 = min(temp3, temp1)
	temp5 = max(temp4, temp2)
	temp0 = -1 * temp0
	temp3 = max(temp2, temp4)
	temp4 = temp0 * temp2
	if temp5 != 0:
		temp5 = temp1 % temp5
	else:
		temp5 = temp5
	return [temp1, temp5]
