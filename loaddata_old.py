import csv
import string

outfile = 'load_cypher'
dire = 'data/data/'

relations1 = ['users', 'tweets', 'hashtags']
relations2 = ['follows', 'sent', 'mentions', 'contains']


# +
#relat = 'match'    #loop
# -

import os.path
if(os.path.isfile(outfile)): 
	file = open(outfile,"r+")
	file. truncate(0)
	file. close()

for relat in relations1:
	str1 = relat[0].upper() + relat[1:-1]
	print (str1)

'''
old_qu = 'delete from '
for relat in reversed(relations):
	qu = old_qu
	qu = qu + relat + ';'
	with open(outfile, 'a') as f:
		print(qu, file=f)
	#print(qu)
'''

for relat in relations1:
	str1 = relat[0].upper() + relat[1:-1]
	with open(dire + relat + '.csv', newline='') as csvfile:
		stud = csv.DictReader(csvfile)
		old_qu = 'CREATE (:' + str1 + ' {'	
	
		for row in stud:
			qu = old_qu
			for key, value in row.items():
				key1 = key		
				#if(key1 == 'id'):
				#	continue				

				if(str1 == 'Tweet' and key1 == 'tweet'):
					key1 = 'text'	
				if(str1 == 'Hashtag'and key1 == 'hashtag'):
					key1 = 'tag'	

				if(value == 'NULL'):
					qu = qu + 'null,'
				else:
					try:
						qu = qu + ' ' + key1 + ': ' + str(int(value)) + ','    
					except ValueError:
						qu = qu + ' ' + key1 + ': ' + '\"' + value + '\",'    
					
					
			qu = qu[:-1] + '});'
			print(qu)
			with open(outfile, 'a') as f:
				print(qu, file=f)
			#print(qu)


relat = 'follows'
str2 = relat[0].upper() + relat[1:]
	
with open(dire + relat + '.csv', newline='') as csvfile:
	stud = csv.DictReader(csvfile)
	old_qu1 = 'MATCH' 
	old_qu2 = 'CREATE ('
		
	for row in stud:
		qu1 = old_qu1
		qu2 = old_qu2
		i = 1
		for key, value in row.items():
			if(value == 'NULL'):
				qu1 = qu1 + 'null,'
			else:
				#print(key)
				#print(key[5])
				try:
					qu1 = qu1 + ' (' + 'user' + str(i) + ': ' + 'User' + '{ ' + 'id' + ': ' + str(int(value)) + '}),'                         
				except ValueError:
					qu1 = qu1 + ' (' + 'user' + str(i) + ': ' + 'User' + '{ ' + 'id' + ': ' + '\"' + value + '\"' + '}),'      
					
			qu2 = 'CREATE (user1)-[:' + str2 + ']->(user2);'
			i = i + 1
			#qu1 = qu1[:-1] + '});'
			#qu2 = qu2[:-1] + '});'
		qu1 = qu1[:-1]
		print(qu1)
		print(qu2)
		
		with open(outfile, 'a') as f:
			print(qu1, file=f)
			print(qu2, file=f)
		#print(qu)

relat = 'sent'
str2 = relat[0].upper() + relat[1:]
	
with open(dire + relat + '.csv', newline='') as csvfile:
	stud = csv.DictReader(csvfile)
	old_qu1 = 'MATCH' 
	old_qu2 = 'CREATE ('
		
	for row in stud:
		qu1 = old_qu1
		qu2 = old_qu2
		i = 1
		for key, value in row.items():
			if(value == 'NULL'):
				qu1 = qu1 + 'null,'
			else:
				#print(key)
				#print(key[5])
				if(i == 1):
					try:
						qu1 = qu1 + ' (' + 'user' + ': ' + 'User' + '{ ' + 'id' + ': ' + str(int(value)) + '}),'                         
					except ValueError:
						qu1 = qu1 + ' (' + 'user' + ': ' + 'User' + '{ ' + 'id' + ': ' + '\"' + value + '\"' + '}),'      
					
				if(i == 2):
					try:
						qu1 = qu1 + ' (' + 'tweet' + ': ' + 'Tweet' + '{ ' + 'id' + ': ' + str(int(value)) + '})'                         
					except ValueError:
						qu1 = qu1 + ' (' + 'tweet' + ': ' + 'Tweet' + '{ ' + 'id' + ': ' + '\"' + value + '\"' + '})' 
							
				qu2 = 'CREATE (user)-[:' + str2 + ']->(tweet);'
				i = i + 1
		
		#qu1 = qu1[:-1] + '});'
		#qu2 = qu2[:-1] + '});'
		print(qu1)
		print(qu2)
			
		with open(outfile, 'a') as f:
			print(qu1, file=f)
			print(qu2, file=f)
		#print(qu)

relat = 'mentions'
str2 = relat[0].upper() + relat[1:]
	
with open(dire + relat + '.csv', newline='') as csvfile:
	stud = csv.DictReader(csvfile)
	old_qu1 = 'MATCH' 
	old_qu2 = 'CREATE ('
		
	for row in stud:
		qu1 = old_qu1
		qu2 = old_qu2
		i = 1
		for key, value in row.items():
			if(value == 'NULL'):
				qu1 = qu1 + 'null,'
			else:
				#print(key)
				#print(key[5])
				if(i == 2):
					try:
						qu1 = qu1 + ' (' + 'user' + ': ' + 'User' + '{ ' + 'id' + ': ' + str(int(value)) + '})'                         
					except ValueError:
						qu1 = qu1 + ' (' + 'user' + ': ' + 'User' + '{ ' + 'id' + ': ' + '\"' + value + '\"' + '})'      
					
				if(i == 1):
					try:
						qu1 = qu1 + ' (' + 'tweet' + ': ' + 'Tweet' + '{ ' + 'id' + ': ' + str(int(value)) + '}),'                         
					except ValueError:
						qu1 = qu1 + ' (' + 'tweet' + ': ' + 'Tweet' + '{ ' + 'id' + ': ' + '\"' + value + '\"' + '}),' 
						
			qu2 = 'CREATE (tweet)-[:' + str2 + ']->(user);'
			i = i + 1
		
		#qu1 = qu1[:-1] + '});'
		#qu2 = qu2[:-1] + '});'
		print(qu1)
		print(qu2)
			
		with open(outfile, 'a') as f:
			print(qu1, file=f)
			print(qu2, file=f)
		#print(qu)

relat = 'contains'
str2 = relat[0].upper() + relat[1:]
	
with open(dire + relat + '.csv', newline='') as csvfile:
	stud = csv.DictReader(csvfile)
	old_qu1 = 'MATCH' 
	old_qu2 = 'CREATE ('
		
	for row in stud:
		qu1 = old_qu1
		qu2 = old_qu2
		i = 1
		for key, value in row.items():
			if(value == 'NULL'):
				qu1 = qu1 + 'null,'
			else:
				#print(key)
				#print(key[5])
				if(i == 2):
					try:
						qu1 = qu1 + ' (' + 'hashtag' + ': ' + 'Hashtag' + '{ ' + 'id' + ': ' + str(int(value)) + '})'                         
					except ValueError:
						qu1 = qu1 + ' (' + 'hashtag' + ': ' + 'Hashtag' + '{ ' + 'id' + ': ' + '\"' + value + '\"' + '})'      
					
				if(i == 1):
					try:
						qu1 = qu1 + ' (' + 'tweet' + ': ' + 'Tweet' + '{ ' + 'id' + ': ' + str(int(value)) + '}),'                         
					except ValueError:
						qu1 = qu1 + ' (' + 'tweet' + ': ' + 'Tweet' + '{ ' + 'id' + ': ' + '\"' + value + '\"' + '}),' 
							
			qu2 = 'CREATE(tweet)-[:' + str2 + ']->(hashtag);'
			i = i + 1
		#qu1 = qu1[:-1] + '});'
		#qu2 = qu2[:-1] + '});'
		print(qu1)
		print(qu2)
			
		with open(outfile, 'a') as f:
			print(qu1, file=f)
			print(qu2, file=f)
		#print(qu)









