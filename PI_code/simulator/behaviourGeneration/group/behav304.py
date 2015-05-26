#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	temp1 = -1 * otherHunter[1]
	temp1 = min( temp0 , otherHunter[1] )
	return [ dist , otherHunter[0] ]
