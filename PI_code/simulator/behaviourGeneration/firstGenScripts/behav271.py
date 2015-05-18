#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	if temp0 != 0:
		temp1 = prey[0] / temp0
	else:
		temp1 = temp0
	if prey[1] > prey[1]:
		temp1 = -1 * temp0
	else:
		if temp0 != 0:
			temp1 = temp0 % temp0
		else:
			temp1 = temp0
	temp2 = temp1 + prey[1]
	temp1 = temp2 * temp0
	temp1 = prey[1] + temp1
	if temp1 != 0:
		temp3 = temp2 % temp1
	else:
		temp3 = temp1
	temp0 = prey[1] - temp0
	temp4 = min(temp3, temp0)
	temp2 = -1 * temp2
	temp3 = min(temp0, temp1)
	if temp2 != 0:
		temp1 = prey[0] / temp2
	else:
		temp1 = temp2
	temp4 = temp0 + temp0
	temp2 = temp3 + prey[1]
	temp5 = temp1 * temp1
	temp3 = min(temp3, temp4)
	if prey[1] != 0:
		temp6 = temp2 % prey[1]
	else:
		temp6 = prey[1]
	temp7 = prey[0] * temp4
	temp8 = temp7 + temp3
	if temp0 > prey[1]:
		temp1 = temp0 * temp4
	else:
		temp1 = -1 * temp5
	temp4 = max(temp4, temp3)
	temp9 = temp8 + temp5
	return [temp5, temp3]
