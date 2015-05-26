#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	temp1 = max(temp0, temp0)
	temp2 = temp0 - prey[1]
	temp2 = max(prey[1], temp2)
	temp2 = prey[1] - temp0
	temp3 = -1 * temp2
	temp4 = min(temp2, prey[1])
	if temp4 != 0:
		temp2 = temp2 / temp4
	else:
		temp2 = temp4
	if temp3 != 0:
		temp4 = temp4 % temp3
	else:
		temp4 = temp3
	temp1 = min(temp2, temp4)
	temp0 = -1 * temp0
	if temp0 > temp3:
		if prey[0] != 0:
			temp0 = temp3 / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = -1 * temp4
	if prey[1] != 0:
		temp5 = prey[1] / prey[1]
	else:
		temp5 = prey[1]
	temp3 = max(prey[1], temp4)
	if temp5 != 0:
		temp4 = prey[1] / temp5
	else:
		temp4 = temp5
	return [temp0, temp2]
