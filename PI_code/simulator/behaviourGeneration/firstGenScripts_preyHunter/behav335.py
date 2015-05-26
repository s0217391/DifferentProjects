#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	if temp0 > prey[1]:
		if prey[0] != 0:
			temp1 = prey[0] % prey[0]
		else:
			temp1 = prey[0]
	else:
		temp1 = prey[1] - prey[0]
	temp2 = prey[0] - prey[0]
	temp2 = -1 * prey[1]
	temp0 = max(prey[1], temp2)
	temp2 = min(prey[0], temp1)
	temp2 = temp0 * prey[1]
	temp3 = -1 * prey[0]
	temp4 = min(prey[0], temp3)
	temp3 = temp3 + temp0
	if temp1 != 0:
		temp0 = temp0 / temp1
	else:
		temp0 = temp1
	if temp2 > temp2:
		if temp2 != 0:
			temp5 = prey[0] % temp2
		else:
			temp5 = temp2
	else:
		temp5 = prey[0] + temp0
	temp0 = prey[0] + temp3
	temp1 = min(temp1, temp4)
	temp0 = max(prey[1], temp5)
	temp5 = temp2 - prey[0]
	temp0 = temp0 - temp4
	if temp3 != 0:
		temp6 = temp4 % temp3
	else:
		temp6 = temp3
	if temp3 != 0:
		temp0 = prey[1] / temp3
	else:
		temp0 = temp3
	temp7 = min(temp3, temp3)
	temp3 = temp6 + temp5
	temp5 = temp2 * temp3
	if temp1 != 0:
		temp7 = temp7 % temp1
	else:
		temp7 = temp1
	temp8 = min(temp1, temp0)
	return [temp3, temp6]
