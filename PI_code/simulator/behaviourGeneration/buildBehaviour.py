#!/usr/bin/python
import sys
import expressionBuilder as eb

def writeLine(f, st = '', tabs = 0):
	result = ""
	for i in range(tabs):
		result = result + "	"
	result = result + st
	f.write(result)
	f.write('\n')
	
def startFile(f):
	writeLine(f, '#!/usr/bin/python');
	writeLine(f, 'import sys');
	writeLine(f, 'import numpy as np')
	writeLine(f)
	writeLine(f, "def compute(prey):")

def main(argv=None):
	newscript = open("generatedBehaviour.py", 'w')
	startFile(newscript)
	lines = eb.generateCodeBlock(seed = 195, minlns = 3, maxlns = 25)
	for x in lines:
		writeLine(newscript, x, 1)
	
if __name__ == "__main__":
	sys.exit(main())
