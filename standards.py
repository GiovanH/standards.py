import argparse
import os
import random

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('integers',type=int, help='The number of iterations')
parser.add_argument('--date')
args = parser.parse_args()

formats = {}

formats['date'] = [
	{'p':'Hour (12)',		'f':'%I'}, #12 hour hour
	{'p':'XM',		'f':'%p'}, #AM or PM
	{'p':'xm',		'f':'%P'}, #am or pm
	{'p':'Day Of Week',		'f':'%u'}, #Day of week
	{'p':'Quarter Of Year',		'f':'%q'}, #Quarter of year
	{'p':'Week Number',		'f':'%U'}, #Week number
	{'p':'Year',		'f':'%Y'}, #Year
	{'p':'Month',		'f':'%m'}, #Month
	{'p':'Day',		'f':'%d'}, #Day
	{'p':'Hour (24)',		'f':'%H'}, #24 hour hour
	{'p':'Minute',		'f':'%M'}, #Minute
	{'p':'Second',		'f':'%S'}  #Second
	]

formats['seperators'] = [
	#{'p':'','f':''},
	{'p':'Dash','f':'-'},
	{'p':'Slash','f':'/'},
	#{'p':'Backslash','f':'\\'},
	{'p':'Space','f':' '},
	{'p':'Underscore','f':'_'}
	]

if args.integers == -1: args.integers = len(formats['date'])

output = ""
outputfmtcode = ""
for i in range(args.integers, 0, -1):
	try:
		choice = random.choice(formats['date'])
	except:
		break
	formats['date'].remove(choice)
	output += choice['p']
	outputfmtcode += choice['f']
	if i != 1:
		choice = random.choice(formats['seperators'])
		#formats['seperators'].remove(choice)
		output += ", " + choice['p'] + ", "
		outputfmtcode += choice['f']

print(output)
#print(outputfmtcode)
os.system("bash -c 'date +\"" + outputfmtcode + "\"'")