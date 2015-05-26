#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[1]
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	temp2 = temp1 * temp0
	temp3 = -1 * temp1
	temp4 = min(prey[1], temp3)
	temp0 = min(temp0, temp1)
	temp3 = temp1 - temp1
	if temp3 != 0:
		temp0 = temp3 / temp3
	else:
		temp0 = temp3
	temp5 = min(temp3, temp2)
	if temp3 > temp1:
		if temp4 != 0:
			temp1 = temp1 / temp4
		else:
			temp1 = temp4
	else:
		temp1 = temp1 - prey[0]
	if prey[0] != 0:
		temp4 = temp0 / prey[0]
	else:
		temp4 = prey[0]
	if temp4 != 0:
		temp1 = temp1 / temp4
	else:
		temp1 = temp4
	temp3 = min(prey[1], temp2)
	temp3 = -1 * temp2
	temp3 = temp0 + temp0
	if prey[1] != 0:
		temp6 = temp4 / prey[1]
	else:
		temp6 = prey[1]
	temp7 = temp0 * temp3
	temp5 = max(temp6, temp4)
	if temp2 > temp0:
		temp4 = -1 * temp2
	else:
		temp4 = prey[0] - temp5
	if temp4 != 0:
		temp4 = temp1 / temp4
	else:
		temp4 = temp4
	temp7 = temp5 + prey[1]
	temp2 = min(temp2, temp3)
	if temp7 > temp7:
		temp2 = temp1 - temp5
	else:
		temp2 = prey[0] * temp0
	temp3 = min(temp2, temp0)
	return [temp3, temp6]
