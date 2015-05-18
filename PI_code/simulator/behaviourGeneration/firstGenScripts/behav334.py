#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	temp1 = temp0 * prey[0]
	temp0 = temp1 + prey[1]
	temp2 = prey[0] * prey[1]
	temp0 = temp2 + temp2
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	temp1 = max(temp0, prey[1])
	temp2 = -1 * prey[0]
	if temp2 > temp0:
		temp3 = max(temp1, temp0)
	else:
		temp3 = max(temp1, prey[1])
	temp1 = prey[1] - temp2
	if prey[1] != 0:
		temp4 = prey[0] / prey[1]
	else:
		temp4 = prey[1]
	if temp2 > prey[0]:
		if temp2 != 0:
			temp5 = temp1 / temp2
		else:
			temp5 = temp2
	else:
		temp5 = max(temp3, temp0)
	if temp1 != 0:
		temp3 = prey[1] % temp1
	else:
		temp3 = temp1
	temp2 = min(prey[1], prey[1])
	if temp2 != 0:
		temp6 = temp1 / temp2
	else:
		temp6 = temp2
	return [temp4, temp3]
