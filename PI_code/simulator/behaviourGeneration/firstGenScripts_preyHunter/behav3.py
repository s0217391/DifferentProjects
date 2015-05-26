#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if temp0 > prey[1]:
		if prey[0] != 0:
			temp1 = prey[1] / prey[0]
		else:
			temp1 = prey[0]
	else:
		if temp0 != 0:
			temp1 = prey[1] % temp0
		else:
			temp1 = temp0
	temp0 = prey[1] + prey[1]
	temp2 = max(prey[0], prey[1])
	temp0 = max(temp1, temp2)
	if temp1 != 0:
		temp3 = prey[1] % temp1
	else:
		temp3 = temp1
	temp4 = -1 * temp2
	temp4 = max(temp1, temp1)
	temp4 = min(temp4, temp1)
	if prey[1] != 0:
		temp5 = temp2 % prey[1]
	else:
		temp5 = prey[1]
	temp1 = -1 * temp5
	temp2 = -1 * temp2
	if temp0 != 0:
		temp3 = temp2 / temp0
	else:
		temp3 = temp0
	if temp4 != 0:
		temp6 = temp5 / temp4
	else:
		temp6 = temp4
	if temp3 != 0:
		temp1 = temp0 % temp3
	else:
		temp1 = temp3
	temp7 = prey[1] + temp5
	temp7 = min(prey[0], prey[1])
	temp6 = prey[0] + prey[0]
	if prey[1] > temp1:
		temp2 = temp1 + prey[1]
	else:
		if prey[1] != 0:
			temp2 = prey[0] / prey[1]
		else:
			temp2 = prey[1]
	if temp7 != 0:
		temp4 = temp6 % temp7
	else:
		temp4 = temp7
	temp6 = max(temp4, prey[1])
	if temp3 > temp3:
		temp4 = temp2 - temp0
	else:
		temp4 = prey[0] + prey[1]
	temp1 = temp7 + temp3
	temp8 = temp4 * temp0
	return [temp5, temp2]
