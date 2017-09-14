import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
        try:
                fH = open(dbfilename, 'rb')
        except FileNotFoundError as e:
                print("New DB: ", dbfilename)
                return []

        # scdb = []
        try:
                scdb =  pickle.load(fH)
                for p in scdb:
                        p['Age'] = int(p['Age'])
                        p['Score'] = int(p['Score'])
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
                        record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                        scdb += [record]
                elif parse[0] == 'del':
                        i = 0
                        while i < len(scdb):
                                if scdb[i]['Name'] == parse[1]:
                                        del(scdb[i])
                                else:
                                        i += 1
                elif parse[0] == 'show':
                        sortKey ='Name' if len(parse) == 1 else parse[1]
                        showScoreDB(scdb, sortKey)
                elif parse[0] == 'find':
                        arr = []
                        sortKey ='Name'
                        for q in scdb:
                                if q['Name'] == parse[1]:
                                       arr.append(q)
                                       showScoreDB(arr, sortKey)
                                       del(arr[0])
                elif parse[0] == 'inc':
                        for q in scdb:
                                if q['Name'] == parse[1]:
                                         q['Score'] += int(parse[2]) 
                elif parse[0] == 'quit':
                        break
                else:
                        print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
        for p in sorted(scdb, key=lambda person: person[keyname]):
                for attr in sorted(p):
                        if attr == 'Name':
                                print(attr + "=" + p[attr], end=' ')
                        elif attr == 'Age' or attr == 'Score':
                                print(attr, "=", int(p[attr]),end=' ') 
                print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

