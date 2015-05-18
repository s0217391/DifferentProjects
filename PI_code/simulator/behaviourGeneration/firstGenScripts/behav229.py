#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp2 = -1 * prey[0]
	temp1 = -1 * temp2
	temp3 = min(temp0, temp0)
	temp3 = -1 * temp1
	if temp2 > prey[1]:
		temp2 = min(temp0, prey[0])
	else:
		temp2 = temp3 + temp1
	temp4 = min(temp0, temp0)
	temp4 = temp1 + prey[0]
	temp4 = temp3 * temp2
	temp5 = temp4 + temp3
	if temp0 > temp4:
		temp5 = max(temp4, temp2)
	else:
		temp5 = prey[0] * temp3
	temp6 = -1 * prey[0]
	temp3 = min(temp5, temp1)
	temp3 = min(temp4, temp0)
	temp1 = -1 * prey[1]
	if temp3 != 0:
		temp3 = temp3 / temp3
	else:
		temp3 = temp3
	temp1 = min(temp6, temp2)
	temp4 = min(temp2, prey[1])
	temp5 = prey[0] + temp2
	temp2 = prey[0] + temp5
	if temp1 != 0:
		temp1 = temp4 / temp1
	else:
		temp1 = temp1
	temp7 = -1 * temp6
	temp3 = temp0 * temp1
	return [temp5, prey[0]]
