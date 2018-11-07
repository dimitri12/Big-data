#!/usr/bin/python
import sys
import json
import re
import simplejson
from pprint import pprint
data=[]
dataobj=''
han_count =0
hon_count =0
hen_count =0
den_count=0
det_count=0
denna_count=0
detta_count=0
i=0
with open('/home/ubuntu/tweets/files/tweets_11.txt') as json_file:
	try:
		for lines in json_file:
			dataobj=lines.split()
			data.append(dataobj)
        except ValueError:
            sys.stderr.write('Could not parse JSON file: {0}'.format('/home/ubuntu/tweets/files/tweets_10.txt'))

RT = data[2][5][68]+data[2][5][69]

data2 = ",".join(map(str,data))
#print data2
match = re.findall(r'\bhan\b|\bhon\b|\bhen\b|\bden\b|\bdet\b|\bdenna\b|\bdenne\b', data2)
#datafile.close()
for word in match:
	if(word == 'han'):
		han_count = han_count +1
	elif(word == 'hon'):
                hon_count = hon_count +1
	elif(word == 'hen'):
                hen_count = hen_count +1
	elif(word == 'den'):
                den_count = den_count +1
	elif(word == 'det'):
                det_count = det_count +1
	elif(word == 'denna'):
                denna_count = denna_count +1
	else: detta_count = detta_count +1

print '%s\t%s' % ("han",han_count)
print '%s\t%s' % ("hon",hon_count)
print '%s\t%s' % ("hen",hen_count)
print '%s\t%s' % ("den",den_count)
print '%s\t%s' % ("det",det_count)
print '%s\t%s' % ("denna",denna_count)
print '%s\t%s' % ("detta",detta_count)

