#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = prey[0] - prey[0]
	temp2 = prey[1] + prey[0]
	temp1 = temp0 * temp0
	temp1 = temp2 + temp1
	temp1 = min(temp0, prey[0])
	temp1 = max(prey[0], prey[0])
	temp2 = prey[0] - prey[0]
	if temp1 != 0:
		temp2 = temp0 % temp1
	else:
		temp2 = temp1
	temp3 = prey[0] * temp1
	temp0 = temp3 + temp3
	if temp2 != 0:
		temp0 = prey[0] % temp2
	else:
		temp0 = temp2
	if temp3 > temp3:
		temp0 = prey[0] - temp3
	else:
		temp0 = max(temp0, prey[1])
	temp4 = prey[0] + prey[1]
	temp5 = -1 * prey[0]
	if temp3 > temp1:
		if prey[1] != 0:
			temp4 = temp3 / prey[1]
		else:
			temp4 = prey[1]
	else:
		temp4 = max(temp0, temp0)
	return [temp5, prey[0]]
