#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[0]
	temp1 = prey[0] + prey[0]
	if temp0 != 0:
		temp2 = prey[0] % temp0
	else:
		temp2 = temp0
	temp1 = prey[1] - prey[0]
	temp3 = temp2 * temp2
	if prey[1] != 0:
		temp3 = temp0 / prey[1]
	else:
		temp3 = prey[1]
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	temp1 = max(temp0, temp2)
	temp3 = prey[0] + prey[0]
	if prey[0] > temp3:
		temp3 = max(temp1, temp3)
	else:
		temp3 = -1 * prey[0]
	temp4 = -1 * temp2
	temp5 = max(temp4, prey[1])
	if temp2 > temp3:
		temp3 = min(temp5, temp0)
	else:
		temp3 = prey[0] - temp3
	if prey[1] > temp2:
		if temp1 != 0:
			temp0 = prey[1] / temp1
		else:
			temp0 = temp1
	else:
		temp0 = temp0 + prey[1]
	if temp1 != 0:
		temp5 = temp5 % temp1
	else:
		temp5 = temp1
	temp4 = max(temp3, prey[0])
	temp1 = -1 * temp0
	if temp4 != 0:
		temp0 = temp2 % temp4
	else:
		temp0 = temp4
	temp6 = max(temp0, temp3)
	if temp0 != 0:
		temp2 = prey[1] / temp0
	else:
		temp2 = temp0
	temp2 = temp0 + temp3
	temp7 = prey[1] - temp6
	return [temp4, temp7]
