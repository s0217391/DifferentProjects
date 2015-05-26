#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	temp1 = min(prey[0], prey[1])
	temp0 = temp0 - temp1
	if temp1 != 0:
		temp2 = prey[1] / temp1
	else:
		temp2 = temp1
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	if temp2 > prey[1]:
		if prey[1] != 0:
			temp3 = prey[1] / prey[1]
		else:
			temp3 = prey[1]
	else:
		if temp0 > prey[1]:
			temp3 = temp0 - temp2
		else:
			temp3 = prey[1] + temp1
	temp4 = min(prey[1], prey[1])
	temp4 = temp2 + temp1
	if temp2 > temp4:
		temp3 = -1 * temp0
	else:
		if prey[0] != 0:
			temp3 = prey[1] / prey[0]
		else:
			temp3 = prey[0]
	temp1 = temp4 * temp1
	if temp0 != 0:
		temp3 = temp2 / temp0
	else:
		temp3 = temp0
	temp3 = max(prey[1], temp1)
	temp2 = prey[0] + temp2
	temp2 = -1 * temp1
	temp0 = min(temp4, temp4)
	if temp3 != 0:
		temp3 = prey[0] % temp3
	else:
		temp3 = temp3
	if temp2 > prey[1]:
		temp4 = -1 * prey[1]
	else:
		temp4 = temp2 + prey[1]
	return [temp2, prey[1]]
