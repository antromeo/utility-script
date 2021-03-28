import os
import sys
import re

def main():
	if(sys.argv[-1]=='--help'):
		print("input valid example: python convert-srt-to-text.py file.srt")
		print("--nonewline append text without newline")
		return
	if len(sys.argv)!=2 and len(sys.argv)!=3:
		print("input valid example: python convert-srt-to-text.py file.srt")
		return 
	#read file line by line
	file = open(sys.argv[1], "r")
	lines = file.readlines()
	file.close()

	text = ''
	for line in lines:
		if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}',line) is None and re.search('^$', line) is None:
			text+=' ' + line
	namefile = str(sys.argv[1]);
	outputfile = open("output-"+os.path.basename(namefile[:-4])+ ".txt", "w+")
	outputfile.write(text)
	if sys.argv[-1]=='--nonewline':
		nonewline=text.replace('\n', ' ').replace('\r', ' ')
		outputfile.write("\n\nTEXT WITHOUT NEWLINE:\n\n"+nonewline)
	print("DONE!!!")
	outputfile.close()
main()
