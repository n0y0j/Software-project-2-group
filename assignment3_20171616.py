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
                                if int(parse[2]) and int(parse[3]):
                                        record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                                        scdb += [record]
                        except ValueError:
                                print("Age또는 Score 값이 올바르지 않습니다. 다시 입력해주세요")
                elif parse[0] == 'find':
                        for i in scdb:
                                try:
                                        if i['Name'] == parse[1]:
                                                for k,v in sorted(i.items()):
                                                        print(k +"="+ v, end= ' ')
                                                print()
                                except KeyError:
                                        print("1")
                                else:
                                        print("2")
                                        
                elif parse[0] == 'del':
                        for p in range(len(scdb)):
                                for i in scdb :
                                        if i['Name'] == parse[1]:
                                                scdb.remove(i)                
                elif parse[0] == 'inc':
                                try:
                                        for i in scdb:
                                                if i['Name'] == parse[1] and int(parse[2]):
                                                        k = int(parse[2]) + int(i['Score'])
                                                        i['Score'] = str(k)
                                                else:
                                                        4/0

                                except (ValueError,ZeroDivisionError):
                                        print("Score에 더하는 수나 이름이 올바르지 않습니다. 다시 입력해주세요")
                elif parse[0] == 'show':
                        try:
                                sortKey ='Name' if len(parse) == 1 else parse[1]
                                showScoreDB(scdb, sortKey)
                        except KeyError:
                                print("Key값이 올바르지 않습니다. 다시 입력해주세요")
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

