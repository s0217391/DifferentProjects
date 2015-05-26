#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	temp1 = -1 * temp0
	temp0 = max(prey[1], prey[1])
	temp2 = temp1 + prey[0]
	if prey[0] != 0:
		temp2 = prey[0] / prey[0]
	else:
		temp2 = prey[0]
	if prey[1] != 0:
		temp3 = prey[0] % prey[1]
	else:
		temp3 = prey[1]
	temp4 = prey[0] + temp3
	if temp4 > temp3:
		temp5 = -1 * prey[1]
	else:
		temp5 = prey[1] * temp0
	if temp0 != 0:
		temp1 = temp4 % temp0
	else:
		temp1 = temp0
	if temp3 != 0:
		temp6 = temp0 % temp3
	else:
		temp6 = temp3
	if prey[0] != 0:
		temp6 = temp6 % prey[0]
	else:
		temp6 = prey[0]
	temp2 = min(temp3, temp3)
	temp3 = max(prey[1], prey[0])
	temp1 = min(temp5, temp1)
	if temp1 != 0:
		temp4 = prey[0] / temp1
	else:
		temp4 = temp1
	if temp1 > temp5:
		temp7 = temp4 + temp4
	else:
		temp7 = temp4 - temp1
	temp5 = temp4 - temp6
	if prey[1] > temp5:
		temp3 = temp1 + prey[0]
	else:
		if temp7 != 0:
			temp3 = temp2 / temp7
		else:
			temp3 = temp7
	temp8 = -1 * temp1
	temp1 = temp1 + temp3
	if temp4 != 0:
		temp0 = temp8 % temp4
	else:
		temp0 = temp4
	temp2 = temp6 - prey[1]
	temp5 = min(temp5, temp0)
	if prey[1] != 0:
		temp0 = temp2 / prey[1]
	else:
		temp0 = prey[1]
	temp5 = temp7 - temp4
	return [temp0, temp5]
