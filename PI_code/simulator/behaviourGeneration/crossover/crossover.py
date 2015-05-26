#!/usr/bin/python
import sys
import random as r

def getRandomSplitPoint(count):
	total = r.randint(4, count - 2)
	return total
	
def isIfElse(nextline):
	if nextline.count('\t') >= 2: return True
	words = nextline.split();
	if len(words) == 0: return False
	if words[0] == "if": return True
	if words[0] == "else:" or words[0] == "else": return True
	return False
	

def copyStart(nbOfLines, rfile, wfile):
	for i in range(0, nbOfLines):	
		l = rfile.readline()
		wfile.write(l)
	nextline = rfile.readline()
	while isIfElse(nextline):
		wfile.write(nextline)
		nextline = rfile.readline()
	

def copyEnd(startline, rfile, wfile):
	i = 0
	inIfElse = False
	writtenOnce = False
	for line in rfile:				
		if isIfElse(line):
			inIfElse = True	
		else:
			inIfElse = False
		if i > startline and (writtenOnce or not inIfElse):
			wfile.write(line)
			writtenOnce = True		
		i += 1	

def checkVarNames(newname):
	wrongfile = open(newname, 'r')
	corrected = open("corrected.py", 'w')
	accepted = ['prey[0]', 'prey[1]', 'otherHunter[0]', 'otherHunter[1]', 'dist']
	nonTerminalAccepted = ['min(', 'max(', 'else:']
	i = -1	
	for line in wrongfile:
		i += 1		
		if i < 4:
			corrected.write(line)
			continue	
			
		tabcount = line.count('\t')
		words = line.split();		
		if len(words) == 0: 
			corrected.write(line)
			continue
		firstw = words[0]
		if accepted.count(firstw) == 0 and firstw != "if" and firstw != "else:":
			accepted.append(firstw)
		for j, w in enumerate(words):
			if len(w) < 4: continue
			if accepted.count(w) == 0 and nonTerminalAccepted.count(w) == 0:
				print words[j]
				words[j] = accepted[r.randint(0, len(accepted) - 1)]
				print words[j]
		correctedline = ''
		for esther in range(0, tabcount): correctedline = correctedline + '\t'
		for w in words:
			correctedline = correctedline + w + ' '
		correctedline = correctedline + '\n'
		corrected.write(correctedline)
			
			
def main(argv=None):
	r1fname = 'behav2.py'
	r2fname = 'behav6.py'
	newname = 'newBehav.py'

	r1linecount = sum(1 for line in open(r1fname))
	r2linecount = sum(1 for line in open(r2fname))

	splitr1 = getRandomSplitPoint(r1linecount)
	splitr2 = getRandomSplitPoint(r2linecount)

	r1 = open(r1fname, 'r')
	r2 = open(r2fname, 'r')
	w = open(newname, 'w')

	copyStart(splitr1, r1, w)
	copyEnd(splitr2, r2, w)
	w.close()

	checkVarNames(newname)



if __name__ == "__main__":
	sys.exit(main())
