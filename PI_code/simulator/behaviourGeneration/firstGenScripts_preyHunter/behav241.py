#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[0]
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	if temp0 > temp0:
		temp1 = prey[1] * temp1
	else:
		temp1 = max(temp1, prey[1])
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	temp2 = min(prey[0], temp1)
	temp3 = prey[0] + prey[0]
	temp1 = max(prey[0], prey[1])
	temp2 = temp0 - temp1
	temp2 = -1 * temp1
	if temp2 != 0:
		temp4 = temp3 % temp2
	else:
		temp4 = temp2
	temp1 = max(prey[0], prey[1])
	if temp0 != 0:
		temp2 = temp2 % temp0
	else:
		temp2 = temp0
	temp1 = -1 * temp0
	temp1 = -1 * temp4
	temp5 = min(temp2, prey[1])
	temp5 = temp3 + prey[1]
	temp5 = min(temp0, temp4)
	temp0 = -1 * temp3
	if prey[1] != 0:
		temp1 = temp3 % prey[1]
	else:
		temp1 = prey[1]
	if temp3 > temp0:
		temp1 = temp5 + prey[1]
	else:
		temp1 = -1 * prey[0]
	temp3 = max(temp3, prey[1])
	temp4 = min(temp4, prey[0])
	return [temp3, prey[0]]
