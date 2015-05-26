#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	if prey[1] > prey[0] :
		temp1 = max( temp0 , prey[1] )
	else:
		if prey[1] > otherHunter[1] :
			if otherHunter[0] != 0:
				temp1 = otherHunter[1] % otherHunter[0]
			else:
				temp1 = otherHunter[0]
		else:
			temp1 = otherHunter[0] + otherHunter[1]
	temp1 = -1 * dist
	return [ temp1 , otherHunter[1] ]
