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
	writeLine(f)
	writeLine(f, "def compute(prey):")

def main(argv=None):
	for i in range(0, 500):
		newscript = open("firstGenScripts/behav" + str(i + 1) + ".py", 'w')
		startFile(newscript)
		lines = eb.generateCodeBlock(seed = i, minlns = 3, maxlns = 25)
		for x in lines:
			(line, tabs) = x
			writeLine(newscript, line, tabs + 1)
	
if __name__ == "__main__":
	sys.exit(main())
