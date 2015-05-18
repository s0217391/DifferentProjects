#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(prey[1], prey[0])
	if temp1 > temp0:
		temp0 = temp0 + temp1
	else:
		temp0 = temp1 * temp1
	if temp0 != 0:
		temp2 = prey[1] / temp0
	else:
		temp2 = temp0
	if prey[1] != 0:
		temp3 = temp1 % prey[1]
	else:
		temp3 = prey[1]
	temp3 = max(prey[1], temp2)
	temp4 = min(temp0, prey[1])
	if temp1 > prey[0]:
		temp5 = temp4 + temp2
	else:
		temp5 = temp1 * temp4
	temp5 = temp1 * temp1
	temp5 = temp4 + temp2
	if temp0 != 0:
		temp2 = temp1 / temp0
	else:
		temp2 = temp0
	if prey[1] != 0:
		temp6 = prey[1] / prey[1]
	else:
		temp6 = prey[1]
	if temp3 != 0:
		temp5 = temp0 / temp3
	else:
		temp5 = temp3
	temp0 = temp6 * temp5
	temp7 = -1 * temp2
	temp5 = min(prey[1], temp4)
	temp1 = temp6 + temp1
	temp5 = min(temp7, temp4)
	temp1 = temp3 + temp5
	if temp1 != 0:
		temp7 = prey[0] % temp1
	else:
		temp7 = temp1
	temp8 = min(temp3, temp0)
	temp3 = min(temp3, temp2)
	temp8 = prey[0] + temp8
	if temp7 > temp0:
		temp7 = -1 * temp6
	else:
		temp7 = min(temp0, temp4)
	return [temp0, prey[0]]
