import os
import socket
from collections import Counter

Counter = Counter()

def findIPAddress():
    hostname = socket.gethostname()
    IP_address = socket.gethostbyname(hostname)
    return IP_address

def getNumberOfWords(file):
    totalwordcount = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                totalwordcount = totalwordcount + len(line.replace("Â", "").split())
    return totalwordcount

TextFilesWordCounts = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")

outputString="Output from a text file at location: /home/output/result.txt:\n\na. Text files present at location: /home/data\n"
for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        outputString=outputString+eachFile+"\n"
        TextFilesWordCounts[eachFile] = getNumberOfWords(path + "/" + eachFile)
		
outputString=outputString+"\n"
outputString=outputString+"b. Total number of words in each text files\n"
AllFilesWordCount = 0
AllFilesNames = ""
for eachkey in TextFilesWordCounts.keys():
    AllFilesNames = AllFilesNames + eachkey + ","
    AllFilesWordCount = AllFilesWordCount + TextFilesWordCounts.get(eachkey)
    outputString = outputString +"Total number of words in (" + eachkey + ") is : " + str(TextFilesWordCounts.get(eachkey))+"\n"

outputString = outputString +"\n"
outputString = outputString +"c. Total number of words in both files\n"
outputString = outputString +"Total number of words in both files (" + AllFilesNames[0:len(AllFilesNames) - 1] + ") is: " + str(AllFilesWordCount)+"\n"

outputString = outputString +"\n"
outputString = outputString +"d. Top 3 words with maximum number of counts in IF.txt\n"

l = Counter.most_common(3)
for k,v in l:
    outputString = outputString + str(k) + ": " + str(v) + "\n"
# outputString = outputString +str(Counter.most_common(3))+"\n"

outputString = outputString +"\n"
outputString = outputString +"e. IP address of your machine\n"
outputString = outputString +"Your IP Address is: " + findIPAddress()

resultsTextFile = open(path + "/" +"result.txt","w")
resultsTextFile.write(outputString)
resultsTextFile.close()
for eachline in open(path + "/" +"result.txt","r").readlines():
    print(eachline.replace("\n",""))