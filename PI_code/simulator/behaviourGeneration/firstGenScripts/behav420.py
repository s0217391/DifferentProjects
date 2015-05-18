#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[0] + temp0
	temp0 = prey[1] + prey[0]
	temp2 = max(temp0, temp0)
	temp0 = temp0 - prey[0]
	temp0 = prey[1] + temp2
	if temp1 != 0:
		temp3 = temp0 / temp1
	else:
		temp3 = temp1
	if temp0 != 0:
		temp4 = temp3 / temp0
	else:
		temp4 = temp0
	temp2 = prey[0] - temp1
	temp2 = temp2 + temp1
	temp1 = max(temp2, temp2)
	temp5 = max(temp3, prey[1])
	temp0 = prey[1] - prey[1]
	if prey[1] > temp5:
		temp5 = max(temp5, temp4)
	else:
		temp5 = temp3 + prey[1]
	temp0 = max(temp3, temp0)
	if temp5 > temp4:
		temp6 = temp3 * temp0
	else:
		if prey[1] != 0:
			temp6 = temp3 / prey[1]
		else:
			temp6 = prey[1]
	temp4 = temp6 - prey[0]
	return [temp1, temp1]
