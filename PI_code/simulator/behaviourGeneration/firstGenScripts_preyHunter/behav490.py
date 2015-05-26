#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = min(prey[0], temp0)
	if prey[0] != 0:
		temp2 = temp1 % prey[0]
	else:
		temp2 = prey[0]
	if temp2 > prey[0]:
		if prey[1] != 0:
			temp3 = temp2 % prey[1]
		else:
			temp3 = prey[1]
	else:
		temp3 = prey[0] + prey[1]
	temp1 = temp3 + temp3
	temp3 = prey[1] + temp2
	temp0 = prey[1] + prey[1]
	temp4 = min(temp0, prey[1])
	if temp1 != 0:
		temp4 = prey[0] / temp1
	else:
		temp4 = temp1
	temp5 = temp0 - temp1
	temp2 = temp4 - temp0
	if temp2 > temp5:
		temp2 = -1 * temp0
	else:
		temp2 = -1 * temp1
	temp5 = -1 * temp2
	temp3 = min(temp3, temp0)
	temp3 = prey[0] + temp4
	if prey[0] > temp3:
		if temp3 != 0:
			temp6 = temp2 / temp3
		else:
			temp6 = temp3
	else:
		temp6 = prey[0] - temp5
	temp1 = temp0 + temp0
	if temp0 > temp0:
		temp5 = temp5 + prey[0]
	else:
		temp5 = temp4 + temp6
	temp7 = -1 * temp1
	if temp7 > temp5:
		if temp5 != 0:
			temp7 = prey[1] / temp5
		else:
			temp7 = temp5
	else:
		temp7 = -1 * temp0
	temp1 = temp2 + temp6
	temp8 = min(temp3, temp1)
	temp2 = max(temp3, temp4)
	temp4 = min(temp0, temp2)
	return [temp5, temp8]
