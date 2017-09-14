import pickle
dbfilename = 'assignment3.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
		
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			try:
				if len(parse) == 4:
					count = 0
					if int(parse[2]) and int(parse[3]):
						count = count + 1
						record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
						scdb += [record]
					else:
						4/0
				else:
					4/0
			except ZeroDivisionError:
				print("Error")
		elif parse[0] == 'del':
			try:
				if len(parse)==2:
					count = 0
					for i in range(len(scdb)):
						for p in scdb:
							if p['Name'] == parse[1]:
								scdb.remove(p)
								count = count + 1
							else:
								continue
					if count == 0:
						4/0
					else:
						continue
				else:
					4/0
			except ZeroDivisionError:
				print("Error")
		elif parse[0] == 'show': #clear
			try:
				if len(parse)==1:
					showScoreDB(scdb, 'Name')
				elif len(parse)==2:
					if parse[1] == 'Age':
						showScoreDB(scdb, 'Age')
					elif parse[1] == 'Score':
						showScoreDB(scdb, 'Score')
					elif parse[1] == 'Name':
						showScoreDB(scdb, 'Name')
					else:
						4/0
				else:
					4/0
			except ZeroDivisionError:
				print("Error")
		elif parse[0] == 'find':
			count =0
			try:
				if len(parse) == 2:
					for i in scdb:
						if i['Name'] == parse[1]:
							count = count + 1
							print('Age' "=" +  i['Age'] + ' Name' "=" +  i['Name'] + ' Score' "=" +  i['Score'], end =' ')
						else:
							continue
					if(count==0):
						4/0
					else:
						continue
				else:
					4/0
			except ZeroDivisionError:
				print("Error")
		elif parse[0] == 'inc':
			count = 0
			try:
				if len(parse)==3:
					for j in scdb:
						if j['Name'] == parse[1]:
							count = count + 1
							a = int(j['Score'])+ int(parse[2])
							j['Score'] = str(a)
						else:
							continue
					if(count ==0):
						4/0
					else:
						continue
				else: #inc가 3단어가 아니면 모두 오류!
					4/0
			except ZeroDivisionError:
				print("Error")
		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

