#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = max(prey[1], prey[1])
	else:
		temp0 = prey[0] + prey[1]
	if prey[0] > prey[1]:
		temp1 = prey[1] + prey[0]
	else:
		if temp0 > prey[1]:
			temp1 = -1 * prey[1]
		else:
			temp1 = min(temp0, prey[1])
	temp0 = max(prey[0], prey[0])
	temp2 = temp0 - temp0
	temp0 = temp1 + temp0
	temp0 = min(temp2, temp0)
	temp3 = prey[0] + temp2
	temp1 = min(temp1, temp1)
	if temp3 != 0:
		temp0 = temp2 % temp3
	else:
		temp0 = temp3
	if temp0 != 0:
		temp1 = temp2 % temp0
	else:
		temp1 = temp0
	if temp3 > temp2:
		if prey[1] != 0:
			temp1 = temp0 / prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = temp2 * prey[1]
	if temp3 != 0:
		temp0 = prey[1] % temp3
	else:
		temp0 = temp3
	if temp0 != 0:
		temp4 = prey[0] / temp0
	else:
		temp4 = temp0
	temp1 = temp0 * prey[0]
	temp3 = min(temp4, temp3)
	temp3 = prey[0] + temp4
	temp0 = temp1 + temp4
	temp3 = max(temp4, prey[0])
	temp2 = temp1 + temp2
	temp3 = max(temp0, temp3)
	temp4 = temp3 + prey[0]
	temp3 = temp2 * temp3
	if temp1 != 0:
		temp1 = temp0 / temp1
	else:
		temp1 = temp1
	return [temp2, prey[1]]
