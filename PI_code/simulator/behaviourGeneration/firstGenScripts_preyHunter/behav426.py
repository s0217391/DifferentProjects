#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	temp1 = prey[0] + temp0
	temp2 = temp1 + temp0
	temp1 = temp2 - temp0
	temp0 = max(prey[0], temp2)
	temp2 = prey[1] * temp1
	temp3 = temp2 + prey[0]
	if prey[1] != 0:
		temp3 = temp0 % prey[1]
	else:
		temp3 = prey[1]
	if temp0 > temp0:
		temp1 = min(prey[1], prey[0])
	else:
		if temp3 != 0:
			temp1 = prey[0] % temp3
		else:
			temp1 = temp3
	if temp2 != 0:
		temp1 = temp0 / temp2
	else:
		temp1 = temp2
	if temp2 != 0:
		temp4 = prey[1] % temp2
	else:
		temp4 = temp2
	return [temp3, temp0]
