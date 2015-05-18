#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[0]
	if temp0 != 0:
		temp1 = prey[1] % temp0
	else:
		temp1 = temp0
	temp1 = prey[1] + prey[1]
	temp0 = prey[1] + temp1
	temp2 = prey[0] - temp1
	temp3 = temp1 * temp1
	if temp3 > temp0:
		temp3 = temp1 - temp3
	else:
		if prey[0] != 0:
			temp3 = temp2 % prey[0]
		else:
			temp3 = prey[0]
	if prey[0] > temp3:
		temp2 = min(prey[1], temp3)
	else:
		temp2 = -1 * temp2
	if temp2 > temp1:
		temp1 = min(temp3, temp2)
	else:
		temp1 = temp3 - temp3
	temp3 = -1 * temp1
	temp4 = temp0 + prey[0]
	temp1 = temp2 + temp2
	if temp3 != 0:
		temp2 = temp1 % temp3
	else:
		temp2 = temp3
	temp3 = temp1 - temp1
	if temp4 != 0:
		temp2 = temp3 / temp4
	else:
		temp2 = temp4
	if temp1 > temp3:
		temp3 = temp1 - prey[1]
	else:
		temp3 = max(temp0, temp1)
	temp4 = temp0 - prey[1]
	if temp3 != 0:
		temp4 = prey[1] % temp3
	else:
		temp4 = temp3
	temp4 = max(temp2, temp2)
	temp0 = temp4 - prey[0]
	temp2 = prey[0] * temp1
	if temp2 != 0:
		temp4 = temp4 % temp2
	else:
		temp4 = temp2
	temp0 = prey[0] - prey[1]
	return [temp3, temp3]
