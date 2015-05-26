#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = -1 * prey[1]
	temp1 = -1 * prey[1]
	temp1 = prey[1] + prey[0]
	temp2 = min(temp1, prey[0])
	if temp0 > temp1:
		temp3 = min(temp1, prey[0])
	else:
		if prey[1] != 0:
			temp3 = temp0 % prey[1]
		else:
			temp3 = prey[1]
	temp3 = min(temp1, temp3)
	if prey[0] > temp1:
		temp0 = prey[1] * prey[1]
	else:
		temp0 = min(temp1, temp1)
	if temp2 != 0:
		temp2 = temp3 % temp2
	else:
		temp2 = temp2
	temp0 = max(temp3, prey[0])
	if temp1 > temp3:
		temp3 = temp2 * temp3
	else:
		if temp1 > temp3:
			if temp3 != 0:
				temp3 = temp1 / temp3
			else:
				temp3 = temp3
		else:
			if temp1 != 0:
				temp3 = temp1 % temp1
			else:
				temp3 = temp1
	temp4 = -1 * temp2
	if temp2 != 0:
		temp5 = prey[1] % temp2
	else:
		temp5 = temp2
	temp4 = temp5 - prey[1]
	temp1 = prey[1] + temp2
	if temp4 != 0:
		temp6 = temp1 % temp4
	else:
		temp6 = temp4
	temp5 = -1 * temp0
	if temp1 != 0:
		temp2 = prey[1] % temp1
	else:
		temp2 = temp1
	if temp5 > temp4:
		temp6 = min(temp4, temp3)
	else:
		temp6 = max(temp4, temp1)
	temp7 = temp6 - temp4
	if temp4 != 0:
		temp8 = temp2 / temp4
	else:
		temp8 = temp4
	if temp4 > temp4:
		temp6 = temp0 + temp0
	else:
		temp6 = temp7 * temp8
	return [temp7, prey[0]]
