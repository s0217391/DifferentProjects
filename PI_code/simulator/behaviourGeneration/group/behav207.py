#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist * dist
	temp1 = prey[1] - otherHunter[1]
	temp2 = otherHunter[0] * dist
	return [ dist , temp2 ]
