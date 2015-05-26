#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = -1 * otherHunter[0]
	temp0 = dist - temp1
	temp0 = temp1 - otherHunter[1]
	temp2 = min( temp1 , otherHunter[0] )
	temp2 = min( temp2 , temp1 )
	return [ dist , otherHunter[0] ]
