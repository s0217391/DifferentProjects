#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[0]
	temp1 = min(prey[1], prey[0])
	temp1 = temp0 - temp1
	temp1 = max(prey[1], prey[0])
	temp1 = min(temp0, prey[0])
	if prey[0] > temp1:
		temp2 = prey[1] + prey[0]
	else:
		temp2 = temp1 - temp1
	if prey[0] != 0:
		temp2 = prey[0] % prey[0]
	else:
		temp2 = prey[0]
	temp1 = max(prey[1], temp1)
	temp0 = max(temp0, prey[0])
	temp3 = temp1 * temp2
	temp1 = temp0 + temp3
	if temp2 != 0:
		temp3 = temp1 / temp2
	else:
		temp3 = temp2
	if temp2 > temp3:
		if temp3 > prey[1]:
			temp1 = min(temp1, prey[0])
		else:
			temp1 = min(temp2, temp0)
	else:
		temp1 = min(prey[0], temp1)
	temp0 = temp1 - temp0
	temp4 = min(prey[1], temp0)
	temp4 = max(temp1, temp2)
	if temp2 != 0:
		temp1 = temp0 % temp2
	else:
		temp1 = temp2
	temp4 = -1 * temp4
	temp3 = prey[1] + temp3
	return [temp1, temp1]
