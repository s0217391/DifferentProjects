#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = -1 * prey[1]
	else:
		temp0 = max(prey[1], prey[0])
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	if prey[0] != 0:
		temp2 = prey[0] % prey[0]
	else:
		temp2 = prey[0]
	if temp0 != 0:
		temp3 = prey[0] / temp0
	else:
		temp3 = temp0
	temp4 = min(temp2, temp3)
	temp4 = max(temp3, temp0)
	temp1 = temp2 + temp4
	if temp1 != 0:
		temp1 = temp3 % temp1
	else:
		temp1 = temp1
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	if temp2 != 0:
		temp5 = temp4 / temp2
	else:
		temp5 = temp2
	temp2 = temp4 * temp3
	if prey[1] != 0:
		temp0 = temp4 % prey[1]
	else:
		temp0 = prey[1]
	if temp0 > temp2:
		temp0 = -1 * prey[0]
	else:
		if prey[0] != 0:
			temp0 = temp0 % prey[0]
		else:
			temp0 = prey[0]
	temp6 = min(temp4, temp4)
	if prey[1] > temp2:
		temp6 = temp3 + temp4
	else:
		if temp3 > temp1:
			temp6 = prey[1] - temp6
		else:
			temp6 = temp6 - temp5
	if temp0 != 0:
		temp7 = temp6 % temp0
	else:
		temp7 = temp0
	temp1 = prey[0] + temp7
	temp0 = -1 * prey[0]
	if temp2 != 0:
		temp8 = temp5 % temp2
	else:
		temp8 = temp2
	temp9 = temp5 * temp6
	temp4 = max(temp6, prey[0])
	temp3 = -1 * temp0
	temp2 = max(prey[1], temp4)
	temp4 = max(temp4, temp6)
	if temp9 > temp9:
		temp5 = -1 * temp9
	else:
		if temp0 != 0:
			temp5 = temp5 % temp0
		else:
			temp5 = temp0
	return [prey[1], temp9]