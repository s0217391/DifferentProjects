#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[0] * temp0
	temp1 = temp1 + temp1
	temp2 = temp0 * temp0
	temp2 = max(temp0, prey[0])
	temp1 = prey[0] + prey[0]
	if prey[0] != 0:
		temp2 = temp2 / prey[0]
	else:
		temp2 = prey[0]
	temp1 = prey[0] - prey[0]
	temp3 = temp0 + temp2
	temp1 = temp3 * temp3
	if prey[1] != 0:
		temp2 = prey[1] % prey[1]
	else:
		temp2 = prey[1]
	temp4 = temp0 + temp2
	if prey[0] > temp2:
		if temp0 != 0:
			temp1 = temp1 / temp0
		else:
			temp1 = temp0
	else:
		temp1 = -1 * prey[0]
	temp0 = temp1 * temp3
	temp0 = max(temp3, temp4)
	temp2 = temp1 - temp4
	temp2 = max(prey[1], temp2)
	if temp1 != 0:
		temp3 = prey[1] % temp1
	else:
		temp3 = temp1
	temp4 = -1 * temp2
	if temp4 != 0:
		temp5 = temp0 % temp4
	else:
		temp5 = temp4
	if temp0 > temp1:
		temp3 = prey[1] + temp2
	else:
		temp3 = min(temp1, temp1)
	if temp2 != 0:
		temp4 = temp5 % temp2
	else:
		temp4 = temp2
	return [temp1, temp1]
