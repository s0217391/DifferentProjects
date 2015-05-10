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
	writeLine(f, "def main(argv=None):")
	
def endFile(f):
	writeLine(f)
	writeLine(f, "if __name__ == '__main__':")
	writeLine(f, "sys.exit(main())", 1)

def main(argv=None):
	newscript = open("newscript", 'w')
	startFile(newscript)
	lines = eb.generateCodeBlock(seed = 195, minlns = 10, maxlns = 25)
	for x in lines:
		writeLine(newscript, x, 1)
	endFile(newscript)
	
if __name__ == "__main__":
	sys.exit(main())
