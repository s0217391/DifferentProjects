#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = max(prey[0], prey[0])
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp2 = min(prey[0], temp0)
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	temp3 = max(prey[1], temp0)
	temp1 = min(temp3, prey[0])
	if prey[1] != 0:
		temp4 = temp1 / prey[1]
	else:
		temp4 = prey[1]
	if temp2 != 0:
		temp4 = temp2 / temp2
	else:
		temp4 = temp2
	if temp1 != 0:
		temp2 = temp4 / temp1
	else:
		temp2 = temp1
	temp3 = prey[1] * temp1
	temp0 = max(temp4, temp3)
	if temp0 > temp3:
		if temp1 > temp3:
			temp3 = max(temp2, temp0)
		else:
			if temp1 != 0:
				temp3 = temp3 % temp1
			else:
				temp3 = temp1
	else:
		temp3 = max(temp0, prey[0])
	temp1 = prey[1] - prey[0]
	if temp3 != 0:
		temp0 = temp3 / temp3
	else:
		temp0 = temp3
	temp2 = min(prey[1], temp1)
	temp4 = prey[0] + temp1
	temp5 = max(prey[1], temp2)
	if temp0 != 0:
		temp2 = temp1 / temp0
	else:
		temp2 = temp0
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	return [temp1, temp4]
