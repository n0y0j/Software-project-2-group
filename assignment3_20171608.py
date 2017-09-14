import sys
fname = input("Enter data file name: ")
try:
    fH = open(fname)
except FileNotFoundError as e:
    print("No such file: " + fname)
    sys.exit()


fH = open(dbfilename, 'rb')
try:
    fH = open(dbfilename)
except FileNotFoundError as e:
    print("New DB: ", dbfilename)
return []
else:
    print("Open DB: ", dbfilename)


def doScoreDB(scdb):
while(True):
inputstr = (input("Score DB > "))
if inputstr == "": continue
parse = inputstr.split(" ")
if parse[0] == 'add':
record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
scdb += [record]
elif parse[0] == 'del':
for p in scdb:
elif parse[0] == 'show':
sortKey ='Name' if len(parse) == 1 else parse[1]
showScoreDB(scdb, sortKey)
if p['Name'] == parse[1]:
scdb.remove(p)
break

elif parse[0] == 'quit':
break
else:
print("Invalid command: " + parse[0])

scdb = []
scdb = 
[{'Age': '19', 'Name': 'Park', 'Score': '79'},
{'Age': '21', 'Name': 'Choi', 'Score': '85'},
{'Age': '21', 'Name': 'Yoon', 'Score': '82'}]
try:
    scdb = pickle.load(fh)
except:
    print("Empty DB: ", dbfilename)
else:
    print("Open DB: ", abfilename)
fh.close()
