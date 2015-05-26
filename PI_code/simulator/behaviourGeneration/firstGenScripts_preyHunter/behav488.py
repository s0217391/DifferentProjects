#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[0]:
		if prey[1] != 0:
			temp0 = prey[1] % prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = max(prey[0], prey[1])
	temp1 = prey[0] - prey[0]
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	temp1 = -1 * temp1
	temp2 = -1 * temp0
	temp3 = prey[1] + temp2
	temp2 = temp1 + temp0
	if prey[0] > prey[1]:
		if prey[0] > temp2:
			temp4 = temp3 * temp2
		else:
			temp4 = min(prey[1], temp3)
	else:
		temp4 = max(temp1, temp1)
	temp5 = -1 * prey[0]
	if temp0 != 0:
		temp4 = prey[0] % temp0
	else:
		temp4 = temp0
	temp6 = temp5 + temp0
	temp2 = prey[1] * temp6
	temp0 = prey[0] - temp4
	temp5 = temp0 + prey[1]
	temp4 = -1 * temp4
	if prey[0] != 0:
		temp5 = temp3 / prey[0]
	else:
		temp5 = prey[0]
	temp0 = min(temp4, temp3)
	temp7 = min(temp2, temp0)
	if temp5 != 0:
		temp8 = temp4 % temp5
	else:
		temp8 = temp5
	if temp4 != 0:
		temp6 = temp8 / temp4
	else:
		temp6 = temp4
	if prey[1] != 0:
		temp6 = temp0 / prey[1]
	else:
		temp6 = prey[1]
	return [temp7, temp8]
