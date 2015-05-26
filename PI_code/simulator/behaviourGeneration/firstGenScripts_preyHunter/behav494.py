#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	if temp1 != 0:
		temp2 = prey[1] / temp1
	else:
		temp2 = temp1
	temp2 = prey[0] - prey[1]
	temp2 = -1 * temp1
	if temp1 != 0:
		temp3 = prey[1] / temp1
	else:
		temp3 = temp1
	temp3 = max(temp2, prey[0])
	temp0 = prey[1] * temp3
	temp4 = -1 * temp3
	temp1 = min(temp0, temp2)
	if temp1 != 0:
		temp2 = temp2 % temp1
	else:
		temp2 = temp1
	temp5 = max(temp1, temp3)
	temp5 = temp2 * temp2
	temp1 = min(prey[0], temp4)
	temp4 = temp1 + temp5
	if prey[0] != 0:
		temp6 = prey[1] % prey[0]
	else:
		temp6 = prey[0]
	temp0 = prey[1] * temp3
	if temp2 > temp4:
		if prey[0] > temp4:
			temp4 = -1 * prey[0]
		else:
			temp4 = min(prey[1], temp1)
	else:
		if prey[1] != 0:
			temp4 = temp1 / prey[1]
		else:
			temp4 = prey[1]
	if temp0 != 0:
		temp7 = temp5 / temp0
	else:
		temp7 = temp0
	temp6 = temp1 - temp4
	temp3 = prey[1] * prey[0]
	temp2 = temp3 - temp7
	if temp1 != 0:
		temp3 = temp3 % temp1
	else:
		temp3 = temp1
	return [prey[0], temp2]
