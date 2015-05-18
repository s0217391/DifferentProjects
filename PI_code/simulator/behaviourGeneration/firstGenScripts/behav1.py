#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	if prey[1] > temp0:
		temp1 = max(temp0, prey[0])
	else:
		temp1 = -1 * temp0
	temp2 = prey[1] * temp1
	temp0 = min(temp2, temp0)
	temp3 = temp1 * temp0
	if prey[0] > temp3:
		temp1 = temp1 * temp3
	else:
		temp1 = prey[0] * temp2
	temp1 = max(prey[0], temp2)
	if temp3 > temp1:
		temp2 = max(temp0, prey[1])
	else:
		temp2 = temp0 - temp1
	if temp3 != 0:
		temp0 = temp3 % temp3
	else:
		temp0 = temp3
	temp4 = max(temp2, temp2)
	temp5 = -1 * temp4
	temp4 = max(temp5, temp4)
	if temp3 != 0:
		temp0 = prey[1] / temp3
	else:
		temp0 = temp3
	temp5 = temp4 - temp4
	temp0 = temp5 - prey[0]
	if temp3 != 0:
		temp3 = temp2 % temp3
	else:
		temp3 = temp3
	temp2 = min(prey[0], temp5)
	temp1 = prey[0] - temp4
	temp2 = temp0 + prey[1]
	temp1 = max(prey[0], prey[1])
	if temp5 != 0:
		temp2 = temp3 % temp5
	else:
		temp2 = temp5
	temp6 = temp0 + temp4
	return [temp1, temp2]
